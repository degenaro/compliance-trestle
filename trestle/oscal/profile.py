# generated by datamodel-codegen:
#   filename:  oscal_profile_schema.json

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import AnyUrl, EmailStr, Field, constr
from trestle.core.base_model import OscalBaseModel


class LocationUuid(OscalBaseModel):
    __root__: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(..., description='References a location defined in metadata.')


class Type(Enum):
    person = 'person'
    organization = 'organization'


class ExternalId(OscalBaseModel):
    scheme: AnyUrl = Field(
        ...,
        description='Indicates the type of external identifier.',
        title='External Identifier Schema',
    )
    id: str


class MemberOfOrganization(OscalBaseModel):
    __root__: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='Identifies that the party object is a member of the organization associated with the provided UUID.',
    )


class PartyUuid(OscalBaseModel):
    __root__: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(..., description='References a party defined in metadata.')


class Base64(OscalBaseModel):
    filename: Optional[str] = Field(
        None,
        description='Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.',
        title='File Name',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Specifies a media type as defined by the Internet Assigned Numbers Authority (IANA) Media Types Registry.',
        title='Media Type',
    )
    value: str


class Link(OscalBaseModel):
    href: str = Field(
        ...,
        description='A resolvable URL reference to a resource.',
        title='Hypertext Reference',
    )
    rel: Optional[str] = Field(
        None,
        description="Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
        title='Relation',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Specifies a media type as defined by the Internet Assigned Numbers Authority (IANA) Media Types Registry.',
        title='Media Type',
    )
    text: Optional[str] = Field(
        None,
        description='A textual label to associate with the link, which may be used for presentation in a tool.',
        title='Link Text',
    )


class Hash(OscalBaseModel):
    algorithm: str = Field(
        ..., description='Method by which a hash is derived', title='Hash algorithm'
    )
    value: str


class Remarks(OscalBaseModel):
    __root__: str = Field(
        ..., description='Additional commentary on the containing object.'
    )


class Published(OscalBaseModel):
    __root__: datetime = Field(
        ...,
        description='The date and time the document was published. The date-time value must be formatted according to RFC 3339 with full time and time zone included.',
    )


class LastModified(OscalBaseModel):
    __root__: datetime = Field(
        ...,
        description='The date and time the document was last modified. The date-time value must be formatted according to RFC 3339 with full time and time zone included.',
    )


class Version(OscalBaseModel):
    __root__: str = Field(
        ...,
        description='A string used to distinguish the current version of the document from other previous (and future) versions.',
    )


class OscalVersion(OscalBaseModel):
    __root__: str = Field(
        ..., description='The OSCAL model version the document was authored against.'
    )


class EmailAddress(OscalBaseModel):
    __root__: EmailStr = Field(
        ..., description='An email address as defined by RFC 5322 Section 3.4.1.'
    )


class TelephoneNumber(OscalBaseModel):
    type: Optional[str] = Field(
        None, description='Indicates the type of phone number.', title='type flag'
    )
    number: str


class AddrLine(OscalBaseModel):
    __root__: str = Field(..., description='A single line of an address.')


class DocumentId(OscalBaseModel):
    scheme: Optional[AnyUrl] = Field(
        None,
        description='Qualifies the kind of document identifier using a URI. If the scheme is not provided the value of the element will be interpreted as a string of characters.',
        title='Document Identification Scheme',
    )
    identifier: str


class Test(OscalBaseModel):
    expression: str = Field(
        ...,
        description='A formal (executable) expression of a constraint',
        title='Constraint test',
    )
    remarks: Optional[Remarks] = None


class ParameterConstraint(OscalBaseModel):
    description: Optional[str] = Field(
        None,
        description='A textual summary of the constraint to be applied.',
        title='Constraint Description',
    )
    tests: Optional[List[Test]] = Field(None, min_items=1)


class ParameterGuideline(OscalBaseModel):
    prose: str = Field(
        ...,
        description='Prose permits multiple paragraphs, lists, tables etc.',
        title='Guideline Text',
    )


class ParameterValue(OscalBaseModel):
    __root__: str = Field(..., description='A parameter value or set of values.')


class ParameterSelection(OscalBaseModel):
    how_many: Optional[str] = Field(
        None,
        alias='how-many',
        description='Describes the number of selections that must occur.',
        title='Parameter Cardinality',
    )
    choice: Optional[List[str]] = Field(None, min_items=1)


class Method(Enum):
    use_first = 'use-first'
    merge = 'merge'
    keep = 'keep'


class Combine(OscalBaseModel):
    method: Optional[Method] = Field(
        None,
        description='How clashing controls should be handled',
        title='Combination method',
    )


class AsIs(OscalBaseModel):
    __root__: bool = Field(
        ...,
        description='An As-is element indicates that the controls should be structured in resolution as they are structured in their source catalogs. It does not contain any elements or attributes.',
    )


class Order(Enum):
    keep = 'keep'
    ascending = 'ascending'
    descending = 'descending'


class IncludeAll(OscalBaseModel):
    pass


class WithChildControls(Enum):
    yes = 'yes'
    no = 'no'


class Matching(OscalBaseModel):
    pattern: Optional[str] = Field(
        None,
        description='A glob expression matching the IDs of one or more controls to be selected.',
        title='Pattern',
    )


class SelectControlById(OscalBaseModel):
    with_child_controls: Optional[WithChildControls] = Field(
        None,
        alias='with-child-controls',
        description='When a control is included, whether its child (dependent) controls are also included.',
        title='Include contained controls with control',
    )
    with_ids: Optional[List[str]] = Field(None, alias='with-ids', min_items=1)
    matching: Optional[List[Matching]] = Field(None, min_items=1)


class Remove(OscalBaseModel):
    name_ref: Optional[str] = Field(
        None,
        alias='name-ref',
        description='Identify items to remove by matching their assigned name',
        title='Reference by (assigned) name',
    )
    class_ref: Optional[str] = Field(
        None,
        alias='class-ref',
        description='Identify items to remove by matching their class.',
        title='Reference by class',
    )
    id_ref: Optional[str] = Field(
        None,
        alias='id-ref',
        description='Identify items to remove indicated by their id.',
        title='Reference by ID',
    )
    item_name: Optional[str] = Field(
        None,
        alias='item-name',
        description="Identify items to remove by the name of the item's information element name, e.g. title or prop",
        title='Item Name Reference',
    )
    ns_ref: Optional[str] = Field(
        None,
        alias='ns-ref',
        description="Identify items to remove by the item's ns, which is the namespace associated with a part, or prop.",
        title='Item Namespace Reference',
    )


class Position(Enum):
    before = 'before'
    after = 'after'
    starting = 'starting'
    ending = 'ending'


class Rlink(OscalBaseModel):
    href: str = Field(
        ...,
        description='A resolvable URI reference to a resource.',
        title='Hypertext Reference',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Specifies a media type as defined by the Internet Assigned Numbers Authority (IANA) Media Types Registry.',
        title='Media Type',
    )
    hashes: Optional[List[Hash]] = Field(None, min_items=1)


class Property(OscalBaseModel):
    name: str = Field(
        ...,
        description="A textual label that uniquely identifies a specific attribute, characteristic, or quality of the property's containing object.",
        title='Property Name',
    )
    uuid: Optional[
        constr(
            regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A unique identifier that can be used to reference this property elsewhere in an OSCAL document. A UUID should be consistantly used for a given location across revisions of the document.',
        title='Property Universally Unique Identifier',
    )
    ns: Optional[AnyUrl] = Field(
        None,
        description="A namespace qualifying the property's name. This allows different organizations to associate distinct semantics with the same name.",
        title='Property Namespace',
    )
    value: str = Field(
        ...,
        description='Indicates the value of the attribute, characteristic, or quality.',
        title='Property Value',
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description="A textual label that provides a sub-type or characterization of the property's name. This can be used to further distinguish or discriminate between the semantics of multiple properties of the same object with the same name and ns.",
        title='Property Class',
    )
    remarks: Optional[Remarks] = None


class ResponsibleParty(OscalBaseModel):
    party_uuids: List[PartyUuid] = Field(..., alias='party-uuids', min_items=1)
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    remarks: Optional[Remarks] = None


class Address(OscalBaseModel):
    type: Optional[str] = Field(
        None, description='Indicates the type of address.', title='Address Type'
    )
    addr_lines: Optional[List[AddrLine]] = Field(None, alias='addr-lines', min_items=1)
    city: Optional[str] = Field(
        None,
        description='City, town or geographical region for the mailing address.',
        title='City',
    )
    state: Optional[str] = Field(
        None,
        description='State, province or analogous geographical region for mailing address',
        title='State',
    )
    postal_code: Optional[str] = Field(
        None,
        alias='postal-code',
        description='Postal or ZIP code for mailing address',
        title='Postal Code',
    )
    country: Optional[str] = Field(
        None,
        description='The ISO 3166-1 alpha-2 country code for the mailing address.',
        title='Country Code',
    )


class Part(OscalBaseModel):
    id: Optional[str] = Field(
        None,
        description="A unique identifier for a specific part instance. This identifier's uniqueness is document scoped and is intended to be consistent for the same part across minor revisions of the document.",
        title='Part Identifier',
    )
    name: str = Field(
        ...,
        description="A textual label that uniquely identifies the part's semantic type.",
        title='Part Name',
    )
    ns: Optional[AnyUrl] = Field(
        None,
        description="A namespace qualifying the part's name. This allows different organizations to associate distinct semantics with the same name.",
        title='Part Namespace',
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description="A textual label that provides a sub-type or characterization of the part's name. This can be used to further distinguish or discriminate between the semantics of multiple parts of the same control with the same name and ns.",
        title='Part Class',
    )
    title: Optional[str] = Field(
        None,
        description='A name given to the part, which may be used by a tool for display and navigation.',
        title='Part Title',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    prose: Optional[str] = Field(
        None,
        description='Permits multiple paragraphs, lists, tables etc.',
        title='Part Text',
    )
    parts: Optional[List[Part]] = None
    links: Optional[List[Link]] = Field(None, min_items=1)


class Parameter(OscalBaseModel):
    id: str = Field(
        ...,
        description="A unique identifier for a specific parameter instance. This identifier's uniqueness is document scoped and is intended to be consistent for the same parameter across minor revisions of the document.",
        title='Parameter Identifier',
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description='A textual label that provides a characterization of the parameter.',
        title='Parameter Class',
    )
    depends_on: Optional[str] = Field(
        None,
        alias='depends-on',
        description='Another parameter invoking this one',
        title='Depends on',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    label: Optional[str] = Field(
        None,
        description='A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned.',
        title='Parameter Label',
    )
    usage: Optional[str] = Field(
        None,
        description='Describes the purpose and use of a parameter',
        title='Parameter Usage Description',
    )
    constraints: Optional[List[ParameterConstraint]] = Field(None, min_items=1)
    guidelines: Optional[List[ParameterGuideline]] = Field(None, min_items=1)
    values: Optional[List[ParameterValue]] = Field(None, min_items=1)
    select: Optional[ParameterSelection] = None
    remarks: Optional[Remarks] = None


class Import(OscalBaseModel):
    href: str = Field(
        ...,
        description='A resolvable URL reference to the base catalog or profile that this profile is tailoring.',
        title='Catalog or Profile Reference',
    )
    include_all: Optional[IncludeAll] = Field(None, alias='include-all')
    include_controls: Optional[List[SelectControlById]] = Field(
        None, alias='include-controls', min_items=1
    )
    exclude_controls: Optional[List[SelectControlById]] = Field(
        None, alias='exclude-controls', min_items=1
    )


class InsertControls(OscalBaseModel):
    order: Optional[Order] = Field(
        None,
        description='A designation of how a selection of controls in a profile is to be ordered.',
        title='Order',
    )
    include_all: Optional[IncludeAll] = Field(None, alias='include-all')
    include_controls: Optional[List[SelectControlById]] = Field(
        None, alias='include-controls', min_items=1
    )
    exclude_controls: Optional[List[SelectControlById]] = Field(
        None, alias='exclude-controls', min_items=1
    )


class SetParameter(OscalBaseModel):
    class_: Optional[str] = Field(
        None,
        alias='class',
        description='A textual label that provides a characterization of the parameter.',
        title='Parameter Class',
    )
    depends_on: Optional[str] = Field(
        None,
        alias='depends-on',
        description='Another parameter invoking this one',
        title='Depends on',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    label: Optional[str] = Field(
        None,
        description='A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned.',
        title='Parameter Label',
    )
    usage: Optional[str] = Field(
        None,
        description='Describes the purpose and use of a parameter',
        title='Parameter Usage Description',
    )
    constraints: Optional[List[ParameterConstraint]] = Field(None, min_items=1)
    guidelines: Optional[List[ParameterGuideline]] = Field(None, min_items=1)
    values: Optional[List[ParameterValue]] = Field(None, min_items=1)
    select: Optional[ParameterSelection] = None


class Add(OscalBaseModel):
    position: Optional[Position] = Field(
        None,
        description='Where to add the new content with respect to the targeted element (beside it or inside it)',
        title='Position',
    )
    id_ref: Optional[str] = Field(
        None,
        alias='id-ref',
        description='Target location of the addition.',
        title='Reference by ID',
    )
    title: Optional[str] = Field(
        None,
        description='A name given to the control, which may be used by a tool for display and navigation.',
        title='Title Change',
    )
    params: Optional[List[Parameter]] = Field(None, min_items=1)
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    parts: Optional[List[Part]] = Field(None, min_items=1)


class Revision(OscalBaseModel):
    title: Optional[str] = Field(
        None,
        description='A name given to the document revision, which may be used by a tool for display and navigation.',
        title='Document Title',
    )
    published: Optional[Published] = None
    last_modified: Optional[LastModified] = Field(None, alias='last-modified')
    version: Optional[Version] = None
    oscal_version: Optional[OscalVersion] = Field(None, alias='oscal-version')
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    remarks: Optional[Remarks] = None


class Location(OscalBaseModel):
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A unique identifier that can be used to reference this defined location elsewhere in an OSCAL document. A UUID should be consistently used for a given location across revisions of the document.',
        title='Location Universally Unique Identifier',
    )
    title: Optional[str] = Field(
        None,
        description='A name given to the location, which may be used by a tool for display and navigation.',
        title='Location Title',
    )
    address: Address
    email_addresses: Optional[List[EmailAddress]] = Field(
        None, alias='email-addresses', min_items=1
    )
    telephone_numbers: Optional[List[TelephoneNumber]] = Field(
        None, alias='telephone-numbers', min_items=1
    )
    urls: Optional[List[AnyUrl]] = Field(None, min_items=1)
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    remarks: Optional[Remarks] = None


class Party(OscalBaseModel):
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A unique identifier that can be used to reference this defined location elsewhere in an OSCAL document. A UUID should be consistantly used for a given party across revisions of the document.',
        title='Party Universally Unique Identifier',
    )
    type: Type = Field(
        ...,
        description='A category describing the kind of party the object describes.',
        title='Party Type',
    )
    name: Optional[str] = Field(
        None,
        description='The full name of the party. This is typically the legal name associated with the party.',
        title='Party Name',
    )
    short_name: Optional[str] = Field(
        None,
        alias='short-name',
        description='A short common name, abbreviation, or acronym for the party.',
        title='Party Short Name',
    )
    external_ids: Optional[List[ExternalId]] = Field(
        None, alias='external-ids', min_items=1
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    email_addresses: Optional[List[EmailAddress]] = Field(
        None, alias='email-addresses', min_items=1
    )
    telephone_numbers: Optional[List[TelephoneNumber]] = Field(
        None, alias='telephone-numbers', min_items=1
    )
    addresses: Optional[List[Address]] = Field(None, min_items=1)
    location_uuids: Optional[List[LocationUuid]] = Field(
        None, alias='location-uuids', min_items=1
    )
    member_of_organizations: Optional[List[MemberOfOrganization]] = Field(
        None, alias='member-of-organizations', min_items=1
    )
    remarks: Optional[Remarks] = None


class Role(OscalBaseModel):
    id: str = Field(
        ...,
        description="A unique identifier for a specific role instance. This identifier's uniqueness is document scoped and is intended to be consistent for the same role across minor revisions of the document.",
        title='Role Identifier',
    )
    title: str = Field(
        ...,
        description='A name given to the role, which may be used by a tool for display and navigation.',
        title='Role Title',
    )
    short_name: Optional[str] = Field(
        None,
        alias='short-name',
        description='A short common name, abbreviation, or acronym for the role.',
        title='Role Short Name',
    )
    description: Optional[str] = Field(
        None,
        description="A summary of the role's purpose and associated responsibilities.",
        title='Role Description',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    remarks: Optional[Remarks] = None


class Citation(OscalBaseModel):
    text: str = Field(
        ..., description='A line of citation text.', title='Citation Text'
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    biblio: Optional[Dict[str, Any]] = Field(
        None,
        description='A container for structured bibliographic information. The model of this information is undefined by OSCAL.',
        title='Bibliographic Definition',
    )


class Resource(OscalBaseModel):
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A globally unique identifier that can be used to reference this defined resource elsewhere in an OSCAL document. A UUID should be consistently used for a given resource across revisions of the document.',
        title='Resource Universally Unique Identifier',
    )
    title: Optional[str] = Field(
        None,
        description='A name given to the resource, which may be used by a tool for display and navigation.',
        title='Resource Title',
    )
    description: Optional[str] = Field(
        None,
        description='A short summary of the resource used to indicate the purpose of the resource.',
        title='Resource Description',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    document_ids: Optional[List[DocumentId]] = Field(
        None, alias='document-ids', min_items=1
    )
    citation: Optional[Citation] = Field(
        None,
        description='A citation consisting of end note text and optional structured bibliographic data.',
        title='Citation',
    )
    rlinks: Optional[List[Rlink]] = Field(None, min_items=1)
    base64: Optional[Base64] = Field(
        None,
        description='The Base64 alphabet in RFC 2045 - aligned with XSD.',
        title='Base64',
    )
    remarks: Optional[Remarks] = None


class BackMatter(OscalBaseModel):
    resources: Optional[List[Resource]] = Field(None, min_items=1)


class Group(OscalBaseModel):
    id: Optional[str] = Field(
        None,
        description="A unique identifier for a specific group instance that can be used to reference the group within this and in other OSCAL documents. This identifier's uniqueness is document scoped and is intended to be consistent for the same group across minor revisions of the document.",
        title='Group Identifier',
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description='A textual label that provides a sub-type or characterization of the group.',
        title='Group Class',
    )
    title: str = Field(
        ...,
        description='A name given to the group, which may be used by a tool for display and navigation.',
        title='Group Title',
    )
    params: Optional[List[Parameter]] = Field(None, min_items=1)
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    parts: Optional[List[Part]] = Field(None, min_items=1)
    groups: Optional[List[Group]] = None
    insert_controls: Optional[List[InsertControls]] = Field(
        None, alias='insert-controls', min_items=1
    )


class Alter(OscalBaseModel):
    control_id: Optional[str] = Field(
        None,
        alias='control-id',
        description="Value of the 'id' flag on a target control",
        title='Control ID',
    )
    removes: Optional[List[Remove]] = Field(None, min_items=1)
    adds: Optional[List[Add]] = Field(None, min_items=1)


class Metadata(OscalBaseModel):
    title: str = Field(
        ...,
        description='A name given to the document, which may be used by a tool for display and navigation.',
        title='Document Title',
    )
    published: Optional[Published] = None
    last_modified: LastModified = Field(..., alias='last-modified')
    version: Version
    oscal_version: OscalVersion = Field(..., alias='oscal-version')
    revisions: Optional[List[Revision]] = Field(None, min_items=1)
    document_ids: Optional[List[DocumentId]] = Field(
        None, alias='document-ids', min_items=1
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    roles: Optional[List[Role]] = Field(None, min_items=1)
    locations: Optional[List[Location]] = Field(None, min_items=1)
    parties: Optional[List[Party]] = Field(None, min_items=1)
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    remarks: Optional[Remarks] = None


class Custom(OscalBaseModel):
    groups: Optional[List[Group]] = Field(None, min_items=1)
    insert_controls: Optional[List[InsertControls]] = Field(
        None, alias='insert-controls', min_items=1
    )


class Modify(OscalBaseModel):
    set_parameters: Optional[Dict[str, SetParameter]] = Field(
        None, alias='set-parameters'
    )
    alters: Optional[List[Alter]] = Field(None, min_items=1)


class Merge(OscalBaseModel):
    combine: Optional[Combine] = None
    as_is: Optional[AsIs] = Field(None, alias='as-is')
    custom: Optional[Custom] = None


class Profile(OscalBaseModel):
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A globally unique identifier for this profile instance. This UUID should be changed when this document is revised.',
        title='Catalog Universally Unique Identifier',
    )
    metadata: Metadata
    imports: List[Import] = Field(..., min_items=1)
    merge: Optional[Merge] = None
    modify: Optional[Modify] = None
    back_matter: Optional[BackMatter] = Field(None, alias='back-matter')


class Model(OscalBaseModel):
    profile: Profile


Part.update_forward_refs()
Group.update_forward_refs()
