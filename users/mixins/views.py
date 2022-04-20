class ActionBasedModelViewSetMixin:
    def get_serializer_class(self):
        try:
            return self.action_serializer_class[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
