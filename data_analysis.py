
#######################################################################################################
# color - eg 'blue'
# value format - eg "abc is %s"
#######################################################################################################
def set_barplot_value(axis, value_list, value_format, value_color):
    for i, v in enumerate(value_list):
        bar_label = value_format % v
        axis.text(i, v + 1, bar_label, color = value_color, va = 'center')

#######################################################################################################
# For some specific version of tensorflow and keras, this funcion should be called prior to  
# using keras using tensorflow gpu backend.
#######################################################################################################
def suppress_tensorflow_gpu_with_keras_error():
    import tensorflow as tf
    from keras.backend.tensorflow_backend import set_session
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
    config.log_device_placement = True  # to log device placement (on which device the operation ran)
                                        # (nothing gets printed in Jupyter, only if you run it standalone)
    sess = tf.Session(config = config)
    set_session(sess)  # set this TensorFlow session as the default session for Keras

#######################################################################################################
# A button used to hide code on jupyter notebook page is added after executing this function.
#######################################################################################################
def enable_ipythonnb_code_toggle():
    from IPython.display import display
    from IPython.display import HTML
    import IPython.core.display as di # Example: di.display_html('<h3>%s:</h3>' % str, raw=True)

    # This line will hide code by default when the notebook is exported as HTML
    di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)

    # This line will add a button to toggle visibility of code blocks, for use with the HTML export version
    di.display_html('''<button onclick="jQuery('.input_area').toggle(); jQuery('.prompt').toggle();">Toggle code</button>''', raw=True)


def ignore_warnings():
    import warnings;
    warnings.filterwarnings('ignore');
