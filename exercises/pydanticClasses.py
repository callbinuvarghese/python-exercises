from typing import List, Optional

from pydantic import BaseModel, field_validator, ValidationInfo
class Variant(BaseModel):
    name : str
    sku : str
    available: bool
    price : float

    @field_validator("sku")
    def sku_length(cls, value):
        if len(value) != 7:
            raise ValueError("sku length must be 7")
    
    # If you want to apply the Validator to the fields "name", "comments", "address", "phone"
    @field_validator("name", "sku", "available", "price")
    def validate_all_fields_one_by_one(cls, value: str, info: ValidationInfo):
        # Do the validation instead of printing
        print(f"{cls}: Field value {value}")

        return value  # this is the value written to the class field
    
class Product(BaseModel):
    id : int
    title: str
    variants: Optional[List[Variant]] = None


item1 = Product(
    id=123123,
    title="Cool Shirt",
    variants=[
        Variant(
            name="Small",
            sku="1ABC123",
            available=True,
            price=24.99
        ),
        Variant(
            name="Medium",
            sku="1ABC124",
            #pydantic converts str to bool
            available="False", 
            # pydantic converts str to float
            price="25"
        )
    ]
)

print(item1)