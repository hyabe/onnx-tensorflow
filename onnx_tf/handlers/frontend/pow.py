from onnx_tf.handlers.frontend_handler import FrontendHandler
from onnx_tf.handlers.handler import onnx_op
from onnx_tf.handlers.handler import tf_op
from .math_mixin import BasicMathMixin


@onnx_op("Pow")
@tf_op("Pow")
class Pow(BasicMathMixin, FrontendHandler):

  @classmethod
  def version_1(cls, node, **kwargs):
    return cls.basic_math_op(node, **kwargs)

  @classmethod
  def version_7(cls, node, **kwargs):
    return cls.basic_math_op(node, **kwargs)
