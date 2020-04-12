import abc


class FormalEmailInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_temp_email') and
                callable(subclass.get_temp_email) or
                NotImplemented)

    @abc.abstractmethod
    def get_temp_email(self) -> str:
        """"Get temporary email address"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_activation_link(self) -> str:
        """"Get account activation link"""
        raise NotImplementedError
