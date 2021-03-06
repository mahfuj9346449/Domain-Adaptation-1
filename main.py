import numpy as np
import tensorflow as tf
import argparse
import os
from dann_model import DANN_Model

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--num_epoch', type=int, default=10000)
    parser.add_argument('--final_dim', type=int, default=256)
    parser.add_argument('--num_classes', type=int, default=10)
    parser.add_argument('--learning_rate', type=float, default=0.005)
    parser.add_argument('--model_mode', type=str, default='DA')
    parser.add_argument('--eval_interval', type=int, default=500)
    parser.add_argument('--model_type', type=str, default='WGAN')
    parser.add_argument('--checkpoint_dir', type=str, default='./checkpoint')
    parser.add_argument('--MNIST', type=str2bool, default='y')
    parser.add_argument('--gp', type=str2bool, default='n')

    args = parser.parse_args()
    print(args)

    if not os.path.exists(args.checkpoint_dir):
        os.mkdir(args.checkpoint_dir)
    run_config = tf.ConfigProto()
    run_config.gpu_options.allow_growth = True
    # If you would like tf to automatically choose an existing and supported device to run the operations in case the specified one does not exists, set allow_soft_placement to True
    run_config.allow_soft_placement = True

    from tensorflow.examples.tutorials.mnist import input_data
    mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

    with tf.Session(config=run_config) as sess:
        if args.model_type == 'DANN':
            print('DANN')
            dann = DANN_Model(args, sess, name='DANN', mnist=mnist)
            dann.train()
        elif args.model_type == 'WGAN'
            wgan = WGAN_Model(args, sess, name='WGAN', mnist=mnist)

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y'):
        return True
    else:
        return False

if __name__ == "__main__":    
    main()
