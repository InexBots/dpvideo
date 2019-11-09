from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec
import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []
class Iface(object):
    def getRSAKey(self):
        pass
    def notifyEmailConfirmationResult(self, parameterMap):
        pass
    def registerVirtualAccount(self, locale, encryptedVirtualUserId, encryptedPassword):
        pass
    def requestVirtualAccountPasswordChange(self, virtualMid, encryptedVirtualUserId, encryptedOldPassword, encryptedNewPassword):
        pass
    def requestVirtualAccountPasswordSet(self, virtualMid, encryptedVirtualUserId, encryptedNewPassword):
        pass
    def unregisterVirtualAccount(self, virtualMid):
        pass
class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0
    def getRSAKey(self):
        self.send_getRSAKey()
        return self.recv_getRSAKey()
    def send_getRSAKey(self):
        self._oprot.writeMessageBegin('getRSAKey', TMessageType.CALL, self._seqid)
        args = getRSAKey_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()
    def recv_getRSAKey(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getRSAKey_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getRSAKey failed: unknown result")
    def notifyEmailConfirmationResult(self, parameterMap):
        self.send_notifyEmailConfirmationResult(parameterMap)
        self.recv_notifyEmailConfirmationResult()
    def send_notifyEmailConfirmationResult(self, parameterMap):
        self._oprot.writeMessageBegin('notifyEmailConfirmationResult', TMessageType.CALL, self._seqid)
        args = notifyEmailConfirmationResult_args()
        args.parameterMap = parameterMap
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()
    def recv_notifyEmailConfirmationResult(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = notifyEmailConfirmationResult_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return
    def registerVirtualAccount(self, locale, encryptedVirtualUserId, encryptedPassword):
        self.send_registerVirtualAccount(locale, encryptedVirtualUserId, encryptedPassword)
        return self.recv_registerVirtualAccount()
    def send_registerVirtualAccount(self, locale, encryptedVirtualUserId, encryptedPassword):
        self._oprot.writeMessageBegin('registerVirtualAccount', TMessageType.CALL, self._seqid)
        args = registerVirtualAccount_args()
        args.locale = locale
        args.encryptedVirtualUserId = encryptedVirtualUserId
        args.encryptedPassword = encryptedPassword
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()
    def recv_registerVirtualAccount(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = registerVirtualAccount_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "registerVirtualAccount failed: unknown result")
    def requestVirtualAccountPasswordChange(self, virtualMid, encryptedVirtualUserId, encryptedOldPassword, encryptedNewPassword):
        self.send_requestVirtualAccountPasswordChange(virtualMid, encryptedVirtualUserId, encryptedOldPassword, encryptedNewPassword)
        self.recv_requestVirtualAccountPasswordChange()
    def send_requestVirtualAccountPasswordChange(self, virtualMid, encryptedVirtualUserId, encryptedOldPassword, encryptedNewPassword):
        self._oprot.writeMessageBegin('requestVirtualAccountPasswordChange', TMessageType.CALL, self._seqid)
        args = requestVirtualAccountPasswordChange_args()
        args.virtualMid = virtualMid
        args.encryptedVirtualUserId = encryptedVirtualUserId
        args.encryptedOldPassword = encryptedOldPassword
        args.encryptedNewPassword = encryptedNewPassword
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()
    def recv_requestVirtualAccountPasswordChange(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = requestVirtualAccountPasswordChange_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return
    def requestVirtualAccountPasswordSet(self, virtualMid, encryptedVirtualUserId, encryptedNewPassword):
        self.send_requestVirtualAccountPasswordSet(virtualMid, encryptedVirtualUserId, encryptedNewPassword)
        self.recv_requestVirtualAccountPasswordSet()
    def send_requestVirtualAccountPasswordSet(self, virtualMid, encryptedVirtualUserId, encryptedNewPassword):
        self._oprot.writeMessageBegin('requestVirtualAccountPasswordSet', TMessageType.CALL, self._seqid)
        args = requestVirtualAccountPasswordSet_args()
        args.virtualMid = virtualMid
        args.encryptedVirtualUserId = encryptedVirtualUserId
        args.encryptedNewPassword = encryptedNewPassword
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()
    def recv_requestVirtualAccountPasswordSet(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = requestVirtualAccountPasswordSet_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return
    def unregisterVirtualAccount(self, virtualMid):
        self.send_unregisterVirtualAccount(virtualMid)
        self.recv_unregisterVirtualAccount()
    def send_unregisterVirtualAccount(self, virtualMid):
        self._oprot.writeMessageBegin('unregisterVirtualAccount', TMessageType.CALL, self._seqid)
        args = unregisterVirtualAccount_args()
        args.virtualMid = virtualMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()
    def recv_unregisterVirtualAccount(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = unregisterVirtualAccount_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return
class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["getRSAKey"] = Processor.process_getRSAKey
        self._processMap["notifyEmailConfirmationResult"] = Processor.process_notifyEmailConfirmationResult
        self._processMap["registerVirtualAccount"] = Processor.process_registerVirtualAccount
        self._processMap["requestVirtualAccountPasswordChange"] = Processor.process_requestVirtualAccountPasswordChange
        self._processMap["requestVirtualAccountPasswordSet"] = Processor.process_requestVirtualAccountPasswordSet
        self._processMap["unregisterVirtualAccount"] = Processor.process_unregisterVirtualAccount
    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True
    def process_getRSAKey(self, seqid, iprot, oprot):
        args = getRSAKey_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getRSAKey_result()
        try:
            result.success = self._handler.getRSAKey()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getRSAKey", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()
    def process_notifyEmailConfirmationResult(self, seqid, iprot, oprot):
        args = notifyEmailConfirmationResult_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = notifyEmailConfirmationResult_result()
        try:
            self._handler.notifyEmailConfirmationResult(args.parameterMap)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("notifyEmailConfirmationResult", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()
    def process_registerVirtualAccount(self, seqid, iprot, oprot):
        args = registerVirtualAccount_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = registerVirtualAccount_result()
        try:
            result.success = self._handler.registerVirtualAccount(args.locale, args.encryptedVirtualUserId, args.encryptedPassword)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("registerVirtualAccount", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()
    def process_requestVirtualAccountPasswordChange(self, seqid, iprot, oprot):
        args = requestVirtualAccountPasswordChange_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = requestVirtualAccountPasswordChange_result()
        try:
            self._handler.requestVirtualAccountPasswordChange(args.virtualMid, args.encryptedVirtualUserId, args.encryptedOldPassword, args.encryptedNewPassword)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("requestVirtualAccountPasswordChange", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()
    def process_requestVirtualAccountPasswordSet(self, seqid, iprot, oprot):
        args = requestVirtualAccountPasswordSet_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = requestVirtualAccountPasswordSet_result()
        try:
            self._handler.requestVirtualAccountPasswordSet(args.virtualMid, args.encryptedVirtualUserId, args.encryptedNewPassword)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("requestVirtualAccountPasswordSet", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()
    def process_unregisterVirtualAccount(self, seqid, iprot, oprot):
        args = unregisterVirtualAccount_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = unregisterVirtualAccount_result()
        try:
            self._handler.unregisterVirtualAccount(args.virtualMid)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("unregisterVirtualAccount", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()
class getRSAKey_args(object):
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getRSAKey_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(getRSAKey_args)
getRSAKey_args.thrift_spec = (
)
class getRSAKey_result(object):
    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = RSAKey()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getRSAKey_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(getRSAKey_result)
getRSAKey_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [RSAKey, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
class notifyEmailConfirmationResult_args(object):
    def __init__(self, parameterMap=None,):
        self.parameterMap = parameterMap
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.MAP:
                    self.parameterMap = {}
                    (_ktype962, _vtype963, _size961) = iprot.readMapBegin()
                    for _i965 in range(_size961):
                        _key966 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val967 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.parameterMap[_key966] = _val967
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('notifyEmailConfirmationResult_args')
        if self.parameterMap is not None:
            oprot.writeFieldBegin('parameterMap', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.parameterMap))
            for kiter968, viter969 in self.parameterMap.items():
                oprot.writeString(kiter968.encode('utf-8') if sys.version_info[0] == 2 else kiter968)
                oprot.writeString(viter969.encode('utf-8') if sys.version_info[0] == 2 else viter969)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(notifyEmailConfirmationResult_args)
notifyEmailConfirmationResult_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.MAP, 'parameterMap', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)
class notifyEmailConfirmationResult_result(object):
    def __init__(self, e=None,):
        self.e = e
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('notifyEmailConfirmationResult_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(notifyEmailConfirmationResult_result)
notifyEmailConfirmationResult_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
class registerVirtualAccount_args(object):
    def __init__(self, locale=None, encryptedVirtualUserId=None, encryptedPassword=None,):
        self.locale = locale
        self.encryptedVirtualUserId = encryptedVirtualUserId
        self.encryptedPassword = encryptedPassword
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.encryptedVirtualUserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.encryptedPassword = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('registerVirtualAccount_args')
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 2)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        if self.encryptedVirtualUserId is not None:
            oprot.writeFieldBegin('encryptedVirtualUserId', TType.STRING, 3)
            oprot.writeString(self.encryptedVirtualUserId.encode('utf-8') if sys.version_info[0] == 2 else self.encryptedVirtualUserId)
            oprot.writeFieldEnd()
        if self.encryptedPassword is not None:
            oprot.writeFieldBegin('encryptedPassword', TType.STRING, 4)
            oprot.writeString(self.encryptedPassword.encode('utf-8') if sys.version_info[0] == 2 else self.encryptedPassword)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(registerVirtualAccount_args)
registerVirtualAccount_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'locale', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'encryptedVirtualUserId', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'encryptedPassword', 'UTF8', None, ),  # 4
)
class registerVirtualAccount_result(object):
    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('registerVirtualAccount_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(registerVirtualAccount_result)
registerVirtualAccount_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
class requestVirtualAccountPasswordChange_args(object):
    def __init__(self, virtualMid=None, encryptedVirtualUserId=None, encryptedOldPassword=None, encryptedNewPassword=None,):
        self.virtualMid = virtualMid
        self.encryptedVirtualUserId = encryptedVirtualUserId
        self.encryptedOldPassword = encryptedOldPassword
        self.encryptedNewPassword = encryptedNewPassword
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.virtualMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.encryptedVirtualUserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.encryptedOldPassword = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.encryptedNewPassword = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('requestVirtualAccountPasswordChange_args')
        if self.virtualMid is not None:
            oprot.writeFieldBegin('virtualMid', TType.STRING, 2)
            oprot.writeString(self.virtualMid.encode('utf-8') if sys.version_info[0] == 2 else self.virtualMid)
            oprot.writeFieldEnd()
        if self.encryptedVirtualUserId is not None:
            oprot.writeFieldBegin('encryptedVirtualUserId', TType.STRING, 3)
            oprot.writeString(self.encryptedVirtualUserId.encode('utf-8') if sys.version_info[0] == 2 else self.encryptedVirtualUserId)
            oprot.writeFieldEnd()
        if self.encryptedOldPassword is not None:
            oprot.writeFieldBegin('encryptedOldPassword', TType.STRING, 4)
            oprot.writeString(self.encryptedOldPassword.encode('utf-8') if sys.version_info[0] == 2 else self.encryptedOldPassword)
            oprot.writeFieldEnd()
        if self.encryptedNewPassword is not None:
            oprot.writeFieldBegin('encryptedNewPassword', TType.STRING, 5)
            oprot.writeString(self.encryptedNewPassword.encode('utf-8') if sys.version_info[0] == 2 else self.encryptedNewPassword)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(requestVirtualAccountPasswordChange_args)
requestVirtualAccountPasswordChange_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'virtualMid', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'encryptedVirtualUserId', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'encryptedOldPassword', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'encryptedNewPassword', 'UTF8', None, ),  # 5
)
class requestVirtualAccountPasswordChange_result(object):
    def __init__(self, e=None,):
        self.e = e
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('requestVirtualAccountPasswordChange_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(requestVirtualAccountPasswordChange_result)
requestVirtualAccountPasswordChange_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
class requestVirtualAccountPasswordSet_args(object):
    def __init__(self, virtualMid=None, encryptedVirtualUserId=None, encryptedNewPassword=None,):
        self.virtualMid = virtualMid
        self.encryptedVirtualUserId = encryptedVirtualUserId
        self.encryptedNewPassword = encryptedNewPassword
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.virtualMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.encryptedVirtualUserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.encryptedNewPassword = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('requestVirtualAccountPasswordSet_args')
        if self.virtualMid is not None:
            oprot.writeFieldBegin('virtualMid', TType.STRING, 2)
            oprot.writeString(self.virtualMid.encode('utf-8') if sys.version_info[0] == 2 else self.virtualMid)
            oprot.writeFieldEnd()
        if self.encryptedVirtualUserId is not None:
            oprot.writeFieldBegin('encryptedVirtualUserId', TType.STRING, 3)
            oprot.writeString(self.encryptedVirtualUserId.encode('utf-8') if sys.version_info[0] == 2 else self.encryptedVirtualUserId)
            oprot.writeFieldEnd()
        if self.encryptedNewPassword is not None:
            oprot.writeFieldBegin('encryptedNewPassword', TType.STRING, 4)
            oprot.writeString(self.encryptedNewPassword.encode('utf-8') if sys.version_info[0] == 2 else self.encryptedNewPassword)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(requestVirtualAccountPasswordSet_args)
requestVirtualAccountPasswordSet_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'virtualMid', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'encryptedVirtualUserId', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'encryptedNewPassword', 'UTF8', None, ),  # 4
)
class requestVirtualAccountPasswordSet_result(object):
    def __init__(self, e=None,):
        self.e = e
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('requestVirtualAccountPasswordSet_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(requestVirtualAccountPasswordSet_result)
requestVirtualAccountPasswordSet_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
class unregisterVirtualAccount_args(object):
    def __init__(self, virtualMid=None,):
        self.virtualMid = virtualMid
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.virtualMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('unregisterVirtualAccount_args')
        if self.virtualMid is not None:
            oprot.writeFieldBegin('virtualMid', TType.STRING, 2)
            oprot.writeString(self.virtualMid.encode('utf-8') if sys.version_info[0] == 2 else self.virtualMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(unregisterVirtualAccount_args)
unregisterVirtualAccount_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'virtualMid', 'UTF8', None, ),  # 2
)
class unregisterVirtualAccount_result(object):
    def __init__(self, e=None,):
        self.e = e
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('unregisterVirtualAccount_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
    def validate(self):
        return
    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self == other)
all_structs.append(unregisterVirtualAccount_result)
unregisterVirtualAccount_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs