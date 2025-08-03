class ResultsTransformer:
    """Transforms analysis results with configurable mappings."""
    
    def __init__(self, category_mapping:dict=None, exclude_keys=None, 
                 tuple_extract_keys:list=None, tuple_extract_index = 0):
        """
        Initialize with configurable transformations.
        
        Args:
            category_mapping: Dict to map category values (e.g., {0: 'negative', 1: 'positive'})
            tuple_extract_keys: List of keys where we extract <tuple_extract_key_index> element from tuples
            exclude_keys: Dict of {result_key: [keys_to_exclude]} for specific exclusions
        """
        self.category_mapping = category_mapping or {}
        self.tuple_extract_keys = tuple_extract_keys or []
        self.exclude_keys = exclude_keys or {}
        self.tuple_extract_index = tuple_extract_index
    
    def transform(self, results):
        """Transform raw results into formatted report."""
        final = {}
        
        for key, data in results.items():
            if key in self.tuple_extract_keys:
                final[key] = self._extract_from_tuples(data)
            elif key in self.exclude_keys:
                final[key] = self._filter_keys(data, self.exclude_keys[key])
            else:
                final[key] = self._map_categories(data)
        
        return final
    
    def _extract_from_tuples(self, data):
        """Extract first element from tuples in the data."""
        result = {}
        for key, value_list in data.items():
            if isinstance(value_list, list) and value_list and isinstance(value_list[0], tuple):
                result[key] = [item[self.tuple_extract_index] for item in value_list]
            else:
                result[key] = value_list
        return result
    
    def _filter_keys(self, data, keys_to_exclude):
        """Remove specified keys and map remaining categories."""
        filtered = {k: v for k, v in data.items() if k not in keys_to_exclude}
        return self._map_categories(filtered)
    
    def _map_categories(self, data):
        return {self._map_category_key(k): v for k, v in data.items()}
    
    def _map_category_key(self, key):
        return self.category_mapping.get(key, key)