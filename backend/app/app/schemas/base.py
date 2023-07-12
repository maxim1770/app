from pydantic import BaseModel, ConfigDict, RootModel


class SchemaBase(BaseModel):
    pass


class RootSchemaBase(RootModel):

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class __SchemaInDBBase(SchemaBase):
    model_config = ConfigDict(from_attributes=True)


class SchemaInDBToAssociationBase(__SchemaInDBBase):
    pass


class SchemaInDBBase(__SchemaInDBBase):
    id: int
