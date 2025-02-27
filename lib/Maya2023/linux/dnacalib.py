# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _py3dnacalib
else:
    import _py3dnacalib

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def __new_decorator(factory_func, original_new):
    @staticmethod
    def __new(cls, *args, **kwargs):
# FIXME: while this workaround solves the immediate issue with the set of classes we currently have,
# it will fail for classes that use a factory function but need no parameters at all, in which case
# the factory function will never be invoked, only the original __new__ function.
        if args or kwargs:
            return factory_func(*args, **kwargs)
        return original_new(cls)
    return __new

def __managed_init(self, *args, **kwargs):
    self._args = args
    self._kwargs = kwargs

import dna
class VersionInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def getMajorVersion():
        return _py3dnacalib.VersionInfo_getMajorVersion()

    @staticmethod
    def getMinorVersion():
        return _py3dnacalib.VersionInfo_getMinorVersion()

    @staticmethod
    def getPatchVersion():
        return _py3dnacalib.VersionInfo_getPatchVersion()

    @staticmethod
    def getVersionString():
        return _py3dnacalib.VersionInfo_getVersionString()

    def __init__(self):
        _py3dnacalib.VersionInfo_swiginit(self, _py3dnacalib.new_VersionInfo())
    __swig_destroy__ = _py3dnacalib.delete_VersionInfo

# Register VersionInfo in _py3dnacalib:
_py3dnacalib.VersionInfo_swigregister(VersionInfo)

def VersionInfo_getMajorVersion():
    return _py3dnacalib.VersionInfo_getMajorVersion()

def VersionInfo_getMinorVersion():
    return _py3dnacalib.VersionInfo_getMinorVersion()

def VersionInfo_getPatchVersion():
    return _py3dnacalib.VersionInfo_getPatchVersion()

def VersionInfo_getVersionString():
    return _py3dnacalib.VersionInfo_getVersionString()

class DNACalibDNAReader(dna.Reader):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def create(*args):
        return _py3dnacalib.DNACalibDNAReader_create(*args)

    @staticmethod
    def destroy(instance):
        return _py3dnacalib.DNACalibDNAReader_destroy(instance)

# Register DNACalibDNAReader in _py3dnacalib:
_py3dnacalib.DNACalibDNAReader_swigregister(DNACalibDNAReader)

def DNACalibDNAReader_create(*args):
    return _py3dnacalib.DNACalibDNAReader_create(*args)

def DNACalibDNAReader_destroy(instance):
    return _py3dnacalib.DNACalibDNAReader_destroy(instance)


DNACalibDNAReader.__new__ = __new_decorator(DNACalibDNAReader_create, DNACalibDNAReader.__new__)
DNACalibDNAReader.__del__ = lambda instance: DNACalibDNAReader_destroy(instance)
DNACalibDNAReader.__init__ = __managed_init
del DNACalibDNAReader.create
del DNACalibDNAReader.destroy

class Command(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_Command

    def run(self, output):
        return _py3dnacalib.Command_run(self, output)

# Register Command in _py3dnacalib:
_py3dnacalib.Command_swigregister(Command)

VectorOperation_Interpolate = _py3dnacalib.VectorOperation_Interpolate
VectorOperation_Add = _py3dnacalib.VectorOperation_Add
VectorOperation_Subtract = _py3dnacalib.VectorOperation_Subtract
VectorOperation_Multiply = _py3dnacalib.VectorOperation_Multiply
class CommandSequence(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_CommandSequence

    def __init__(self, *args):
        _py3dnacalib.CommandSequence_swiginit(self, _py3dnacalib.new_CommandSequence(*args))

    def run(self, output):
        return _py3dnacalib.CommandSequence_run(self, output)

    def add(self, command):
        return _py3dnacalib.CommandSequence_add(self, command)

    def remove(self, command):
        return _py3dnacalib.CommandSequence_remove(self, command)

    def contains(self, command):
        return _py3dnacalib.CommandSequence_contains(self, command)

    def size(self):
        return _py3dnacalib.CommandSequence_size(self)

# Register CommandSequence in _py3dnacalib:
_py3dnacalib.CommandSequence_swigregister(CommandSequence)


def command_sequence_init(_init):
    def wrapper(self, *args, **kwargs):
        self._commands = []
        _init(self, *args, **kwargs)
    return wrapper

def command_sequence_add(_add):
    def wrapper(self, command):
        self._commands.append(command)
        _add(self, command)
    return wrapper

def command_sequence_remove(_remove):
    def wrapper(self, command):
        self._commands.remove(command)
        _remove(self, command)
    return wrapper

CommandSequence.__init__ = command_sequence_init(CommandSequence.__init__)
CommandSequence.add = command_sequence_add(CommandSequence.add)
CommandSequence.remove = command_sequence_remove(CommandSequence.remove)

class CalculateMeshLowerLODsCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_CalculateMeshLowerLODsCommand

    def __init__(self, *args):
        _py3dnacalib.CalculateMeshLowerLODsCommand_swiginit(self, _py3dnacalib.new_CalculateMeshLowerLODsCommand(*args))

    def setMeshIndex(self, meshIndex):
        return _py3dnacalib.CalculateMeshLowerLODsCommand_setMeshIndex(self, meshIndex)

    def run(self, output):
        return _py3dnacalib.CalculateMeshLowerLODsCommand_run(self, output)

# Register CalculateMeshLowerLODsCommand in _py3dnacalib:
_py3dnacalib.CalculateMeshLowerLODsCommand_swigregister(CalculateMeshLowerLODsCommand)

class ClearBlendShapesCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_ClearBlendShapesCommand

    def __init__(self, *args):
        _py3dnacalib.ClearBlendShapesCommand_swiginit(self, _py3dnacalib.new_ClearBlendShapesCommand(*args))

    def run(self, output):
        return _py3dnacalib.ClearBlendShapesCommand_run(self, output)

# Register ClearBlendShapesCommand in _py3dnacalib:
_py3dnacalib.ClearBlendShapesCommand_swigregister(ClearBlendShapesCommand)

class PruneBlendShapeTargetsCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_PruneBlendShapeTargetsCommand

    def __init__(self, *args):
        _py3dnacalib.PruneBlendShapeTargetsCommand_swiginit(self, _py3dnacalib.new_PruneBlendShapeTargetsCommand(*args))

    def setThreshold(self, threshold):
        return _py3dnacalib.PruneBlendShapeTargetsCommand_setThreshold(self, threshold)

    def run(self, output):
        return _py3dnacalib.PruneBlendShapeTargetsCommand_run(self, output)

# Register PruneBlendShapeTargetsCommand in _py3dnacalib:
_py3dnacalib.PruneBlendShapeTargetsCommand_swigregister(PruneBlendShapeTargetsCommand)

class RemoveAnimatedMapCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveAnimatedMapCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveAnimatedMapCommand_swiginit(self, _py3dnacalib.new_RemoveAnimatedMapCommand(*args))

    def setAnimatedMapIndex(self, animatedMapIndex):
        return _py3dnacalib.RemoveAnimatedMapCommand_setAnimatedMapIndex(self, animatedMapIndex)

    def setAnimatedMapIndices(self, animatedMapIndices):
        return _py3dnacalib.RemoveAnimatedMapCommand_setAnimatedMapIndices(self, animatedMapIndices)

    def run(self, output):
        return _py3dnacalib.RemoveAnimatedMapCommand_run(self, output)

# Register RemoveAnimatedMapCommand in _py3dnacalib:
_py3dnacalib.RemoveAnimatedMapCommand_swigregister(RemoveAnimatedMapCommand)

class RemoveBlendShapeCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveBlendShapeCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveBlendShapeCommand_swiginit(self, _py3dnacalib.new_RemoveBlendShapeCommand(*args))

    def setBlendShapeIndex(self, blendShapeIndex):
        return _py3dnacalib.RemoveBlendShapeCommand_setBlendShapeIndex(self, blendShapeIndex)

    def setBlendShapeIndices(self, blendShapeIndices):
        return _py3dnacalib.RemoveBlendShapeCommand_setBlendShapeIndices(self, blendShapeIndices)

    def run(self, output):
        return _py3dnacalib.RemoveBlendShapeCommand_run(self, output)

# Register RemoveBlendShapeCommand in _py3dnacalib:
_py3dnacalib.RemoveBlendShapeCommand_swigregister(RemoveBlendShapeCommand)

class RemoveJointAnimationCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveJointAnimationCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveJointAnimationCommand_swiginit(self, _py3dnacalib.new_RemoveJointAnimationCommand(*args))

    def setJointIndex(self, jointIndex):
        return _py3dnacalib.RemoveJointAnimationCommand_setJointIndex(self, jointIndex)

    def setJointIndices(self, jointIndices):
        return _py3dnacalib.RemoveJointAnimationCommand_setJointIndices(self, jointIndices)

    def run(self, output):
        return _py3dnacalib.RemoveJointAnimationCommand_run(self, output)

# Register RemoveJointAnimationCommand in _py3dnacalib:
_py3dnacalib.RemoveJointAnimationCommand_swigregister(RemoveJointAnimationCommand)

class RemoveJointCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveJointCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveJointCommand_swiginit(self, _py3dnacalib.new_RemoveJointCommand(*args))

    def setJointIndex(self, jointIndex):
        return _py3dnacalib.RemoveJointCommand_setJointIndex(self, jointIndex)

    def setJointIndices(self, jointIndices):
        return _py3dnacalib.RemoveJointCommand_setJointIndices(self, jointIndices)

    def run(self, output):
        return _py3dnacalib.RemoveJointCommand_run(self, output)

# Register RemoveJointCommand in _py3dnacalib:
_py3dnacalib.RemoveJointCommand_swigregister(RemoveJointCommand)

class RemoveMeshCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RemoveMeshCommand

    def __init__(self, *args):
        _py3dnacalib.RemoveMeshCommand_swiginit(self, _py3dnacalib.new_RemoveMeshCommand(*args))

    def setMeshIndex(self, meshIndex):
        return _py3dnacalib.RemoveMeshCommand_setMeshIndex(self, meshIndex)

    def setMeshIndices(self, meshIndices):
        return _py3dnacalib.RemoveMeshCommand_setMeshIndices(self, meshIndices)

    def run(self, output):
        return _py3dnacalib.RemoveMeshCommand_run(self, output)

# Register RemoveMeshCommand in _py3dnacalib:
_py3dnacalib.RemoveMeshCommand_swigregister(RemoveMeshCommand)

class RenameAnimatedMapCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RenameAnimatedMapCommand

    def __init__(self, *args):
        _py3dnacalib.RenameAnimatedMapCommand_swiginit(self, _py3dnacalib.new_RenameAnimatedMapCommand(*args))

    def setName(self, *args):
        return _py3dnacalib.RenameAnimatedMapCommand_setName(self, *args)

    def run(self, output):
        return _py3dnacalib.RenameAnimatedMapCommand_run(self, output)

# Register RenameAnimatedMapCommand in _py3dnacalib:
_py3dnacalib.RenameAnimatedMapCommand_swigregister(RenameAnimatedMapCommand)

class RenameBlendShapeCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RenameBlendShapeCommand

    def __init__(self, *args):
        _py3dnacalib.RenameBlendShapeCommand_swiginit(self, _py3dnacalib.new_RenameBlendShapeCommand(*args))

    def setName(self, *args):
        return _py3dnacalib.RenameBlendShapeCommand_setName(self, *args)

    def run(self, output):
        return _py3dnacalib.RenameBlendShapeCommand_run(self, output)

# Register RenameBlendShapeCommand in _py3dnacalib:
_py3dnacalib.RenameBlendShapeCommand_swigregister(RenameBlendShapeCommand)

class RenameJointCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RenameJointCommand

    def __init__(self, *args):
        _py3dnacalib.RenameJointCommand_swiginit(self, _py3dnacalib.new_RenameJointCommand(*args))

    def setName(self, *args):
        return _py3dnacalib.RenameJointCommand_setName(self, *args)

    def run(self, output):
        return _py3dnacalib.RenameJointCommand_run(self, output)

# Register RenameJointCommand in _py3dnacalib:
_py3dnacalib.RenameJointCommand_swigregister(RenameJointCommand)

class RenameMeshCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RenameMeshCommand

    def __init__(self, *args):
        _py3dnacalib.RenameMeshCommand_swiginit(self, _py3dnacalib.new_RenameMeshCommand(*args))

    def setName(self, *args):
        return _py3dnacalib.RenameMeshCommand_setName(self, *args)

    def run(self, output):
        return _py3dnacalib.RenameMeshCommand_run(self, output)

# Register RenameMeshCommand in _py3dnacalib:
_py3dnacalib.RenameMeshCommand_swigregister(RenameMeshCommand)

class RotateCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_RotateCommand

    def __init__(self, *args):
        _py3dnacalib.RotateCommand_swiginit(self, _py3dnacalib.new_RotateCommand(*args))

    def setRotation(self, degrees):
        return _py3dnacalib.RotateCommand_setRotation(self, degrees)

    def setOrigin(self, origin):
        return _py3dnacalib.RotateCommand_setOrigin(self, origin)

    def run(self, output):
        return _py3dnacalib.RotateCommand_run(self, output)

# Register RotateCommand in _py3dnacalib:
_py3dnacalib.RotateCommand_swigregister(RotateCommand)

class ScaleCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_ScaleCommand

    def __init__(self, *args):
        _py3dnacalib.ScaleCommand_swiginit(self, _py3dnacalib.new_ScaleCommand(*args))

    def setScale(self, scale):
        return _py3dnacalib.ScaleCommand_setScale(self, scale)

    def setOrigin(self, origin):
        return _py3dnacalib.ScaleCommand_setOrigin(self, origin)

    def run(self, output):
        return _py3dnacalib.ScaleCommand_run(self, output)

# Register ScaleCommand in _py3dnacalib:
_py3dnacalib.ScaleCommand_swigregister(ScaleCommand)

class SetBlendShapeTargetDeltasCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetBlendShapeTargetDeltasCommand

    def __init__(self, *args):
        _py3dnacalib.SetBlendShapeTargetDeltasCommand_swiginit(self, _py3dnacalib.new_SetBlendShapeTargetDeltasCommand(*args))

    def setMeshIndex(self, meshIndex):
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setMeshIndex(self, meshIndex)

    def setBlendShapeTargetIndex(self, blendShapeTargetIndex):
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setBlendShapeTargetIndex(self, blendShapeTargetIndex)

    def setDeltas(self, *args):
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setDeltas(self, *args)

    def setVertexIndices(self, vertexIndices):
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setVertexIndices(self, vertexIndices)

    def setMasks(self, masks):
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setMasks(self, masks)

    def setOperation(self, operation):
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_setOperation(self, operation)

    def run(self, output):
        return _py3dnacalib.SetBlendShapeTargetDeltasCommand_run(self, output)

# Register SetBlendShapeTargetDeltasCommand in _py3dnacalib:
_py3dnacalib.SetBlendShapeTargetDeltasCommand_swigregister(SetBlendShapeTargetDeltasCommand)
cvar = _py3dnacalib.cvar
SetBlendShapeTargetDeltasCommand.VertexIndicesOutOfBoundsError = _py3dnacalib.cvar.SetBlendShapeTargetDeltasCommand_VertexIndicesOutOfBoundsError
SetBlendShapeTargetDeltasCommand.NoVertexIndicesSetError = _py3dnacalib.cvar.SetBlendShapeTargetDeltasCommand_NoVertexIndicesSetError
SetBlendShapeTargetDeltasCommand.DeltasVertexIndicesCountMismatch = _py3dnacalib.cvar.SetBlendShapeTargetDeltasCommand_DeltasVertexIndicesCountMismatch
SetBlendShapeTargetDeltasCommand.DeltasMasksCountMismatch = _py3dnacalib.cvar.SetBlendShapeTargetDeltasCommand_DeltasMasksCountMismatch

class SetLODsCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetLODsCommand

    def __init__(self, *args):
        _py3dnacalib.SetLODsCommand_swiginit(self, _py3dnacalib.new_SetLODsCommand(*args))

    def setLODs(self, lods):
        return _py3dnacalib.SetLODsCommand_setLODs(self, lods)

    def run(self, output):
        return _py3dnacalib.SetLODsCommand_run(self, output)

# Register SetLODsCommand in _py3dnacalib:
_py3dnacalib.SetLODsCommand_swigregister(SetLODsCommand)

class SetNeutralJointRotationsCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetNeutralJointRotationsCommand

    def __init__(self, *args):
        _py3dnacalib.SetNeutralJointRotationsCommand_swiginit(self, _py3dnacalib.new_SetNeutralJointRotationsCommand(*args))

    def setRotations(self, *args):
        return _py3dnacalib.SetNeutralJointRotationsCommand_setRotations(self, *args)

    def run(self, output):
        return _py3dnacalib.SetNeutralJointRotationsCommand_run(self, output)

# Register SetNeutralJointRotationsCommand in _py3dnacalib:
_py3dnacalib.SetNeutralJointRotationsCommand_swigregister(SetNeutralJointRotationsCommand)

class SetNeutralJointTranslationsCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetNeutralJointTranslationsCommand

    def __init__(self, *args):
        _py3dnacalib.SetNeutralJointTranslationsCommand_swiginit(self, _py3dnacalib.new_SetNeutralJointTranslationsCommand(*args))

    def setTranslations(self, *args):
        return _py3dnacalib.SetNeutralJointTranslationsCommand_setTranslations(self, *args)

    def run(self, output):
        return _py3dnacalib.SetNeutralJointTranslationsCommand_run(self, output)

# Register SetNeutralJointTranslationsCommand in _py3dnacalib:
_py3dnacalib.SetNeutralJointTranslationsCommand_swigregister(SetNeutralJointTranslationsCommand)

class SetSkinWeightsCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetSkinWeightsCommand

    def __init__(self, *args):
        _py3dnacalib.SetSkinWeightsCommand_swiginit(self, _py3dnacalib.new_SetSkinWeightsCommand(*args))

    def setMeshIndex(self, meshIndex):
        return _py3dnacalib.SetSkinWeightsCommand_setMeshIndex(self, meshIndex)

    def setVertexIndex(self, vertexIndex):
        return _py3dnacalib.SetSkinWeightsCommand_setVertexIndex(self, vertexIndex)

    def setWeights(self, weights):
        return _py3dnacalib.SetSkinWeightsCommand_setWeights(self, weights)

    def setJointIndices(self, jointIndices):
        return _py3dnacalib.SetSkinWeightsCommand_setJointIndices(self, jointIndices)

    def run(self, output):
        return _py3dnacalib.SetSkinWeightsCommand_run(self, output)

# Register SetSkinWeightsCommand in _py3dnacalib:
_py3dnacalib.SetSkinWeightsCommand_swigregister(SetSkinWeightsCommand)

class SetVertexPositionsCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_SetVertexPositionsCommand

    def __init__(self, *args):
        _py3dnacalib.SetVertexPositionsCommand_swiginit(self, _py3dnacalib.new_SetVertexPositionsCommand(*args))

    def setMeshIndex(self, meshIndex):
        return _py3dnacalib.SetVertexPositionsCommand_setMeshIndex(self, meshIndex)

    def setPositions(self, *args):
        return _py3dnacalib.SetVertexPositionsCommand_setPositions(self, *args)

    def setMasks(self, masks):
        return _py3dnacalib.SetVertexPositionsCommand_setMasks(self, masks)

    def setOperation(self, operation):
        return _py3dnacalib.SetVertexPositionsCommand_setOperation(self, operation)

    def run(self, output):
        return _py3dnacalib.SetVertexPositionsCommand_run(self, output)

# Register SetVertexPositionsCommand in _py3dnacalib:
_py3dnacalib.SetVertexPositionsCommand_swigregister(SetVertexPositionsCommand)
SetVertexPositionsCommand.PositionsMasksCountMismatch = _py3dnacalib.cvar.SetVertexPositionsCommand_PositionsMasksCountMismatch

class TranslateCommand(Command):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _py3dnacalib.delete_TranslateCommand

    def __init__(self, *args):
        _py3dnacalib.TranslateCommand_swiginit(self, _py3dnacalib.new_TranslateCommand(*args))

    def setTranslation(self, translation):
        return _py3dnacalib.TranslateCommand_setTranslation(self, translation)

    def run(self, output):
        return _py3dnacalib.TranslateCommand_run(self, output)

# Register TranslateCommand in _py3dnacalib:
_py3dnacalib.TranslateCommand_swigregister(TranslateCommand)



