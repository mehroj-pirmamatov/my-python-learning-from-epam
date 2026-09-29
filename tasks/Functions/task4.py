from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters
    """
    filtered_data = selector(data)

    for filter_func in filters:
        filtered_data = filter_func(filtered_data)

    return filtered_data


def select(*columns: str) -> ModifierFunc:
    """
    Return function that selects only specific columns from dataset
    """
    def selector(data: DataType) -> DataType:
        result = []

        for item in data:
            new_item = {}

            for column in columns:
                if column in item:
                    new_item[column] = item[column]

            result.append(new_item)

        return result

    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """
    Return function that filters specific column to be one of values
    """
    def filter_func(data: DataType) -> DataType:
        result = []

        for item in data:
            if column not in item or item[column] in values:
                result.append(item)

        return result

    return filter_func
