# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for trestle replicate command."""
import argparse
import shutil
import sys
from pathlib import Path
from unittest import mock

from tests import test_utils

import trestle.core.err as err
from trestle.cli import Trestle
from trestle.core.commands.replicate import ReplicateCmd
from trestle.oscal.catalog import Catalog
from trestle.utils import fs
from trestle.utils.load_distributed import load_distributed

subcommand_list = [
    'catalog',
    'profile',
    'target-definition',
    'component-definition',
    'system-security-plan',
    'assessment-plan',
    'assessment-results',
    'plan-of-action-and-milestones'
]


def _copy_local(source_model_path, source_model_name, model_alias):
    plural_alias = model_alias if model_alias[-1] == 's' else model_alias + 's'
    full_model_path = source_model_path / plural_alias / source_model_name
    local_model_path = Path(plural_alias) / source_model_name
    shutil.rmtree(local_model_path, ignore_errors=True)
    shutil.copytree(full_model_path, local_model_path)


def test_replicate_cmd_no_file(tmp_trestle_dir: Path) -> None:
    """Confirm failure when file does not exist."""
    for subcommand in subcommand_list:
        test_args = f'trestle replicate {subcommand} -f mock_file_name -o random_named_{subcommand}'.split()
        with mock.patch.object(sys, 'argv', test_args):
            rc = Trestle().run()
            assert rc != 0


def test_replicate_cmd(testdata_dir, tmp_trestle_dir) -> None:
    """Test replicate command."""
    # prepare trestle project dir with the file
    test_utils.ensure_trestle_config_dir(tmp_trestle_dir)

    test_data_source = testdata_dir / 'split_merge/step4_split_groups_array'

    source_name = 'mycatalog'
    rep_name = 'repcatalog'
    _copy_local(test_data_source, source_name, 'catalog')

    catalogs_dir = Path('catalogs/')
    rep_file = catalogs_dir / rep_name / 'catalog.json'

    # execute the command to replicate the model into replicated
    test_args = f'trestle replicate catalog -f {source_name} -o {rep_name}'.split()
    with mock.patch.object(sys, 'argv', test_args):
        rc = Trestle().run()
        assert rc == 0

    # now load the replicate and compare

    rep_model_type, rep_model_alias, rep_model_instance = load_distributed(rep_file)

    expected_model_type, _ = fs.get_contextual_model_type(rep_file.absolute())

    expected_model_instance = Catalog.oscal_read(testdata_dir / 'split_merge/load_distributed/catalog.json')

    assert rep_model_type == expected_model_type
    assert rep_model_alias == 'catalog'
    assert expected_model_instance == rep_model_instance


def test_replicate_cmd_failures(testdata_dir, tmp_trestle_dir) -> None:
    """Test replicate command failure paths."""
    # prepare trestle project dir with the file
    test_utils.ensure_trestle_config_dir(tmp_trestle_dir)
    source_name = 'minimal_catalog'
    test_data_file = testdata_dir / 'json' / (source_name + '.json')
    catalogs_dir = Path('catalogs/')
    local_data_file = catalogs_dir / source_name / 'catalog.json'
    (catalogs_dir / source_name).mkdir()
    shutil.copy(test_data_file, local_data_file)
    rep_name = 'repcatalog'
    rep_file = catalogs_dir / rep_name / 'catalog.json'
    shutil.rmtree(catalogs_dir / rep_name, ignore_errors=True)
    (catalogs_dir / rep_name).mkdir()

    # now create pre-existing replica to force error
    rep_file.touch()

    test_args = f'trestle replicate catalog -f {source_name} -o {rep_name}'.split()
    with mock.patch.object(sys, 'argv', test_args):
        rc = Trestle().run()
        assert rc == 1

    shutil.rmtree(catalogs_dir / rep_name, ignore_errors=True)

    args = argparse.Namespace(file=source_name, output=rep_name, verbose=False)

    # Force PermissionError:
    with mock.patch('trestle.core.commands.replicate.load_distributed') as load_distributed_mock:
        load_distributed_mock.side_effect = PermissionError
        rc = ReplicateCmd.replicate_object('catalog', Catalog, args)
        assert rc == 1

    # Force TrestleError:
    with mock.patch('trestle.core.commands.replicate.load_distributed') as load_distributed_mock:
        load_distributed_mock.side_effect = err.TrestleError('load_distributed_error')
        rc = ReplicateCmd.replicate_object('catalog', Catalog, args)
        assert rc == 1

    with mock.patch('trestle.core.commands.replicate.Plan.execute') as execute_mock:
        with mock.patch('trestle.core.commands.replicate.Plan.simulate') as simulate_mock:
            with mock.patch('trestle.core.commands.replicate.Plan.rollback') as rollback_mock:
                simulate_mock.side_effect = None
                rollback_mock.side_effect = None
                execute_mock.side_effect = err.TrestleError('execute_trestle_error')
                rc = ReplicateCmd.replicate_object('catalog', Catalog, args)
                assert rc == 1

    # Force TrestleError in simulate:
    with mock.patch('trestle.core.commands.replicate.Plan.simulate') as simulate_mock:
        simulate_mock.side_effect = err.TrestleError('simulate_trestle_error')
        rc = ReplicateCmd.replicate_object('catalog', Catalog, args)
        assert rc == 1


def test_replicate_load_file_failure(tmp_trestle_dir: Path) -> None:
    """Test model load failures."""
    test_utils.ensure_trestle_config_dir(tmp_trestle_dir)

    # Create a file with bad json
    sample_data = '"star": {'
    source_dir = Path('catalogs/bad_catalog')
    source_dir.mkdir(exist_ok=True)
    bad_file_path = source_dir / 'catalog.json'
    bad_file = bad_file_path.open('w+', encoding='utf8')
    bad_file.write(sample_data)
    bad_file.close()

    args = 'trestle replicate catalog -f bad_catalog -o rep_bad_catalog'.split()
    with mock.patch.object(sys, 'argv', args):
        rc = Trestle().run()
        assert rc == 1


def test_replicate_file_system(tmp_trestle_dir: Path) -> None:
    """Test model load failures."""
    test_utils.ensure_trestle_config_dir(tmp_trestle_dir)

    args = argparse.Namespace(file='foo', output='bar', verbose=False)
    with mock.patch('trestle.core.commands.replicate.fs.get_trestle_project_root') as get_root_mock:
        get_root_mock.side_effect = [None]
        rc = ReplicateCmd.replicate_object('catalog', Catalog, args)
        assert rc == 1
