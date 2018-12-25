MODEL = 'pixel_rnn'  # either pixel_rnn or pixel_cnn

# Hyperparams
BATCH_SIZE = 100
DIM = 64  # Model dimensionality.
GRAD_CLIP = 1  # Elementwise grad clip threshold

# Dataset
N_CHANNELS = 1
WIDTH = 28
HEIGHT = 28

# Other constants
TEST_BATCH_SIZE = 100  # batch size to use when evaluating on dev/test sets.
# This should be the max that can fit into GPU memory.
EVAL_DEV_COST = True  # whether to evaluate dev cost during training
GEN_SAMPLES = True  # whether to generate samples during training
# (generating samples takes WIDTH*HEIGHT*N_CHANNELS full passes through the net)
TRAIN_MODE = 'iters'  # 'iters' to use PRINT_ITERS and STOP_ITERS, 'time' to use PRINT_TIME and STOP_TIME
PRINT_ITERS = 5000  # Print cost, generate samples, save model checkpoint every N iterations.
STOP_ITERS = 100000  # Stop after this many iterations
PRINT_TIME = 60*60  # Print cost, generate samples, save model checkpoint every N seconds.
STOP_TIME = 60*60*2  # Stop after this many seconds of actual training
# (not including time req'd to generate samples etc.)


def print_model_settings(locals_):
    print("Model settings:")
    all_vars = [(k, v) for (k, v) in locals_.items() if (k.isupper() and k != 'T')]
    all_vars = sorted(all_vars, key=lambda x: x[0])
    for var_name, var_value in all_vars:
        print("\t{}: {}".format(var_name, var_value))


print_model_settings(locals().copy())
