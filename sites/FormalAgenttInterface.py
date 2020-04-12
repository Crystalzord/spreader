import abc


class FormalAgenttInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'register_account') and
                callable(subclass.register_account) and
                hasattr(subclass, 'login') and
                callable(subclass.login) and
                hasattr(subclass, 'logout') and
                callable(subclass.logout) and
                hasattr(subclass, 'create_post') and
                callable(subclass.create_post) and
                hasattr(subclass, 'create_comment') and
                callable(subclass.create_comment) and
                hasattr(subclass, 'like_post') and
                callable(subclass.like_post) and
                hasattr(subclass, 'like_comment') and
                callable(subclass.like_comment) and
                hasattr(subclass, 'dislike_comment') and
                callable(subclass.dislike_comment) or
                NotImplemented)

    @abc.abstractmethod
    def register_account(self, email: str):
        """"Register account using temporary email address"""
        raise NotImplementedError

    @abc.abstractmethod
    def login(self):
        """"doc"""
        raise NotImplementedError

    @abc.abstractmethod
    def logout(self):
        """"doc"""
        raise NotImplementedError

    @abc.abstractmethod
    def create_post(self):
        """"doc"""
        raise NotImplementedError

    @abc.abstractmethod
    def create_comment(self):
        """"doc"""
        raise NotImplementedError

    @abc.abstractmethod
    def like_post(self):
        """"doc"""
        raise NotImplementedError

    @abc.abstractmethod
    def like_comment(self):
        """"doc"""
        raise NotImplementedError

    @abc.abstractmethod
    def dislike_comment(self):
        """"doc"""
        raise NotImplementedError
