# generated by datamodel-codegen:
#   filename:  oscal_component_schema.json

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import AnyUrl, EmailStr, Field, conint, constr
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


class Transport(Enum):
    TCP = 'TCP'
    UDP = 'UDP'


class PortRange(OscalBaseModel):
    start: Optional[conint(ge=0, multiple_of=1)] = Field(
        None,
        description='Indicates the starting port number in a port range',
        title='Start',
    )
    end: Optional[conint(ge=0, multiple_of=1)] = Field(
        None,
        description='Indicates the ending port number in a port range',
        title='End',
    )
    transport: Optional[Transport] = Field(
        None, description='Indicates the transport type.', title='Transport'
    )


class SetParameter(OscalBaseModel):
    values: List[str] = Field(..., min_items=1)
    remarks: Optional[Remarks] = None


class ImportComponentDefinition(OscalBaseModel):
    href: str = Field(
        ...,
        description='A link to a resource that defines a set of components and/or capabilities to import into this collection.',
        title='Hyperlink Reference',
    )


class IncorporatesComponent(OscalBaseModel):
    description: str = Field(
        ...,
        description='A description of the component, including information about its function.',
        title='Component Description',
    )


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


class ResponsibleRole(OscalBaseModel):
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    party_uuids: Optional[List[PartyUuid]] = Field(
        None, alias='party-uuids', min_items=1
    )
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


class Protocol(OscalBaseModel):
    uuid: Optional[
        constr(
            regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A globally unique identifier that can be used to reference this service protocol entry elsewhere in an OSCAL document. A UUID should be consistently used for a given resource across revisions of the document.',
        title='Service Protocol Information Universally Unique Identifier',
    )
    name: str = Field(
        ...,
        description='The common name of the protocol, which should be the appropriate "service name" from the IANA Service Name and Transport Protocol Port Number Registry.',
        title='Protocol Name',
    )
    title: Optional[str] = Field(
        None,
        description='A human readable name for the protocol (e.g., Transport Layer Security).',
        title='Protocol Title',
    )
    port_ranges: Optional[List[PortRange]] = Field(
        None, alias='port-ranges', min_items=1
    )


class Statement(OscalBaseModel):
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A unique identifier for a specific control implementation.',
        title='Control Statement Implementation Identifier',
    )
    description: str = Field(
        ...,
        description='A summary of how the containing control statement is implemented by the component or capability.',
        title='Statement Implementation Description',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(
        None, alias='responsible-roles'
    )
    remarks: Optional[Remarks] = None


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


class ImplementedRequirement(OscalBaseModel):
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A unique identifier for a specific control implementation.',
        title='Control Implementation Identifier',
    )
    control_id: Optional[str] = Field(
        None,
        alias='control-id',
        description='A reference to a control identifier.',
        title='Control Identifier Reference',
    )
    description: str = Field(
        ...,
        description='A description of how the specified control is implemented for the containing component or capability.',
        title='Control Implementation Description',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(
        None, alias='responsible-roles'
    )
    set_parameters: Optional[Dict[str, SetParameter]] = Field(
        None, alias='set-parameters'
    )
    statements: Optional[Dict[str, Statement]] = None
    remarks: Optional[Remarks] = None


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


class ControlImplementation(OscalBaseModel):
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A unique identifier for the set of implemented controls.',
        title='Control Implementation Set Identifier',
    )
    source: str = Field(
        ...,
        description='A reference to an OSCAL catalog or profile providing the referenced control or subcontrol definition.',
        title='Source Resource Reference',
    )
    description: str = Field(
        ...,
        description='A description of how the specified set of controls are implemented for the containing component or capability.',
        title='Control Implementation Description',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    set_parameters: Optional[Dict[str, SetParameter]] = Field(
        None, alias='set-parameters'
    )
    implemented_requirements: List[ImplementedRequirement] = Field(
        ..., alias='implemented-requirements', min_items=1
    )


class DefinedComponent(OscalBaseModel):
    type: str = Field(
        ...,
        description='A category describing the purpose of the component.',
        title='Component Type',
    )
    title: str = Field(
        ...,
        description='A human readable name for the component.',
        title='Component Title',
    )
    description: str = Field(
        ...,
        description='A description of the component, including information about its function.',
        title='Component Description',
    )
    purpose: Optional[str] = Field(
        None,
        description='A summary of the technological or business purpose of the component.',
        title='Purpose',
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(
        None, alias='responsible-roles'
    )
    protocols: Optional[List[Protocol]] = Field(None, min_items=1)
    control_implementations: Optional[List[ControlImplementation]] = Field(
        None, alias='control-implementations', min_items=1
    )
    remarks: Optional[Remarks] = None


class Capability(OscalBaseModel):
    name: str = Field(
        ...,
        description="The capability's human-readable name.",
        title='Capability Name',
    )
    description: str = Field(
        ..., description='A summary of the capability.', title='Capability Description'
    )
    props: Optional[List[Property]] = Field(None, min_items=1)
    links: Optional[List[Link]] = Field(None, min_items=1)
    incorporates_components: Optional[Dict[str, IncorporatesComponent]] = Field(
        None, alias='incorporates-components'
    )
    control_implementations: Optional[List[ControlImplementation]] = Field(
        None, alias='control-implementations', min_items=1
    )
    remarks: Optional[Remarks] = None


class ComponentDefinition(OscalBaseModel):
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A globally unique identifier for this component definition instance. This UUID should be changed when this document is revised.',
        title='Component Definition Universally Unique Identifier',
    )
    metadata: Metadata
    import_component_definitions: Optional[List[ImportComponentDefinition]] = Field(
        None, alias='import-component-definitions', min_items=1
    )
    components: Optional[Dict[str, DefinedComponent]] = None
    capabilities: Optional[Dict[str, Capability]] = None
    back_matter: Optional[BackMatter] = Field(None, alias='back-matter')


class Model(OscalBaseModel):
    component_definition: ComponentDefinition = Field(..., alias='component-definition')
