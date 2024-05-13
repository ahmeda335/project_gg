"""Array-size annotations for OpenGL.raw.GLU

Automatically generated by the generateraw script, do not edit!
"""
from OpenGL.raw import GLU as raw

from ctypes import *
from OpenGL import platform, arrays
from OpenGL.constant import Constant
from OpenGL.raw.GL import _types as GL_types
GLvoid = GL_types.GLvoid



gluCheckExtension = arrays.setInputArraySizeType(
    arrays.setInputArraySizeType(
        raw.gluCheckExtension,
        None, # XXX Could not determine size of argument extName for gluCheckExtension arrays.GLubyteArray
        arrays.GLubyteArray, 
        'extName',
    ),
    None, # XXX Could not determine size of argument extString for gluCheckExtension arrays.GLubyteArray
    arrays.GLubyteArray, 
    'extString',
)

gluGetNurbsProperty = arrays.setInputArraySizeType(
    raw.gluGetNurbsProperty,
    None, # XXX Could not determine size of argument data for gluGetNurbsProperty arrays.GLfloatArray
    arrays.GLfloatArray, 
    'data',
)

gluGetTessProperty = arrays.setInputArraySizeType(
    raw.gluGetTessProperty,
    None, # XXX Could not determine size of argument data for gluGetTessProperty arrays.GLdoubleArray
    arrays.GLdoubleArray, 
    'data',
)

gluLoadSamplingMatrices = arrays.setInputArraySizeType(
    arrays.setInputArraySizeType(
        arrays.setInputArraySizeType(
            raw.gluLoadSamplingMatrices,
            None, # XXX Could not determine size of argument model for gluLoadSamplingMatrices arrays.GLfloatArray
            arrays.GLfloatArray, 
            'model',
        ),
        None, # XXX Could not determine size of argument perspective for gluLoadSamplingMatrices arrays.GLfloatArray
        arrays.GLfloatArray, 
        'perspective',
    ),
    None, # XXX Could not determine size of argument view for gluLoadSamplingMatrices arrays.GLintArray
    arrays.GLintArray, 
    'view',
)

gluNurbsCurve = arrays.setInputArraySizeType(
    arrays.setInputArraySizeType(
        raw.gluNurbsCurve,
        None, # XXX Could not determine size of argument knots for gluNurbsCurve arrays.GLfloatArray
        arrays.GLfloatArray, 
        'knots',
    ),
    None, # XXX Could not determine size of argument control for gluNurbsCurve arrays.GLfloatArray
    arrays.GLfloatArray, 
    'control',
)

gluNurbsSurface = arrays.setInputArraySizeType(
    arrays.setInputArraySizeType(
        arrays.setInputArraySizeType(
            raw.gluNurbsSurface,
            None, # XXX Could not determine size of argument sKnots for gluNurbsSurface arrays.GLfloatArray
            arrays.GLfloatArray, 
            'sKnots',
        ),
        None, # XXX Could not determine size of argument tKnots for gluNurbsSurface arrays.GLfloatArray
        arrays.GLfloatArray, 
        'tKnots',
    ),
    None, # XXX Could not determine size of argument control for gluNurbsSurface arrays.GLfloatArray
    arrays.GLfloatArray, 
    'control',
)

gluPickMatrix = arrays.setInputArraySizeType(
    raw.gluPickMatrix,
    None, # XXX Could not determine size of argument viewport for gluPickMatrix arrays.GLintArray
    arrays.GLintArray, 
    'viewport',
)

gluProject = arrays.setInputArraySizeType(
    arrays.setInputArraySizeType(
        arrays.setInputArraySizeType(
            arrays.setInputArraySizeType(
                arrays.setInputArraySizeType(
                    arrays.setInputArraySizeType(
                        raw.gluProject,
                        None, # XXX Could not determine size of argument model for gluProject arrays.GLdoubleArray
                        arrays.GLdoubleArray, 
                        'model',
                    ),
                    None, # XXX Could not determine size of argument proj for gluProject arrays.GLdoubleArray
                    arrays.GLdoubleArray, 
                    'proj',
                ),
                None, # XXX Could not determine size of argument view for gluProject arrays.GLintArray
                arrays.GLintArray, 
                'view',
            ),
            None, # XXX Could not determine size of argument winX for gluProject arrays.GLdoubleArray
            arrays.GLdoubleArray, 
            'winX',
        ),
        None, # XXX Could not determine size of argument winY for gluProject arrays.GLdoubleArray
        arrays.GLdoubleArray, 
        'winY',
    ),
    None, # XXX Could not determine size of argument winZ for gluProject arrays.GLdoubleArray
    arrays.GLdoubleArray, 
    'winZ',
)

gluPwlCurve = arrays.setInputArraySizeType(
    raw.gluPwlCurve,
    None, # XXX Could not determine size of argument data for gluPwlCurve arrays.GLfloatArray
    arrays.GLfloatArray, 
    'data',
)

gluTessVertex = arrays.setInputArraySizeType(
    raw.gluTessVertex,
    None, # XXX Could not determine size of argument location for gluTessVertex arrays.GLdoubleArray
    arrays.GLdoubleArray, 
    'location',
)

gluUnProject = arrays.setInputArraySizeType(
    arrays.setInputArraySizeType(
        arrays.setInputArraySizeType(
            arrays.setInputArraySizeType(
                arrays.setInputArraySizeType(
                    arrays.setInputArraySizeType(
                        raw.gluUnProject,
                        None, # XXX Could not determine size of argument model for gluUnProject arrays.GLdoubleArray
                        arrays.GLdoubleArray, 
                        'model',
                    ),
                    None, # XXX Could not determine size of argument proj for gluUnProject arrays.GLdoubleArray
                    arrays.GLdoubleArray, 
                    'proj',
                ),
                None, # XXX Could not determine size of argument view for gluUnProject arrays.GLintArray
                arrays.GLintArray, 
                'view',
            ),
            None, # XXX Could not determine size of argument objX for gluUnProject arrays.GLdoubleArray
            arrays.GLdoubleArray, 
            'objX',
        ),
        None, # XXX Could not determine size of argument objY for gluUnProject arrays.GLdoubleArray
        arrays.GLdoubleArray, 
        'objY',
    ),
    None, # XXX Could not determine size of argument objZ for gluUnProject arrays.GLdoubleArray
    arrays.GLdoubleArray, 
    'objZ',
)

gluUnProject4 = arrays.setInputArraySizeType(
    arrays.setInputArraySizeType(
        arrays.setInputArraySizeType(
            arrays.setInputArraySizeType(
                arrays.setInputArraySizeType(
                    arrays.setInputArraySizeType(
                        arrays.setInputArraySizeType(
                            raw.gluUnProject4,
                            None, # XXX Could not determine size of argument model for gluUnProject4 arrays.GLdoubleArray
                            arrays.GLdoubleArray, 
                            'model',
                        ),
                        None, # XXX Could not determine size of argument proj for gluUnProject4 arrays.GLdoubleArray
                        arrays.GLdoubleArray, 
                        'proj',
                    ),
                    None, # XXX Could not determine size of argument view for gluUnProject4 arrays.GLintArray
                    arrays.GLintArray, 
                    'view',
                ),
                None, # XXX Could not determine size of argument objX for gluUnProject4 arrays.GLdoubleArray
                arrays.GLdoubleArray, 
                'objX',
            ),
            None, # XXX Could not determine size of argument objY for gluUnProject4 arrays.GLdoubleArray
            arrays.GLdoubleArray, 
            'objY',
        ),
        None, # XXX Could not determine size of argument objZ for gluUnProject4 arrays.GLdoubleArray
        arrays.GLdoubleArray, 
        'objZ',
    ),
    None, # XXX Could not determine size of argument objW for gluUnProject4 arrays.GLdoubleArray
    arrays.GLdoubleArray, 
    'objW',
)

__all__ = [
    'gluCheckExtension',
    'gluGetNurbsProperty',
    'gluGetTessProperty',
    'gluLoadSamplingMatrices',
    'gluNurbsCurve',
    'gluNurbsSurface',
    'gluPickMatrix',
    'gluProject',
    'gluPwlCurve',
    'gluTessVertex',
    'gluUnProject',
    'gluUnProject4'
]
