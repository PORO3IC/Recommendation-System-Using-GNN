import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Run GAT Config.")
    parser.add_argument('--weights_path', nargs='?', default='',
                        help='')
    parser.add_argument('--data_path', nargs='?', default='../Data/',
                        help='')
    parser.add_argument('--proj_path', nargs='?', default='',
                        help='')
    parser.add_argument('--dataset', nargs='?', default='movie-lens-100k',
                        help='')
    parser.add_argument('--pretrain', type=int, default=0,
                        help='')
    parser.add_argument('--n_layers', type=int, default=1,
                        help='')
    parser.add_argument('--test_att', type=int, default=0,
                        help='')
    parser.add_argument('--verbose', type=int, default=1,
                        help='')
    parser.add_argument('--epoch', type=int, default=200,
                        help='')
    parser.add_argument('--multi_loss', type=int, default=0,
                        help='')
    parser.add_argument('--mc', type=int, default=0,
                        help='')
    parser.add_argument('--use_attribute', type=int, default=0,
                        help='')
    parser.add_argument('--loss_type', type=str, default='bpr',
                        help='')
    parser.add_argument('--opt_level', type=str, default='O1',
                        help='')
    parser.add_argument('--embed_size', type=int, default=64,
                        help='')
    parser.add_argument('--n_heads', type=int, default=4,
                        help='')
    parser.add_argument('--layer_size', nargs='?', default='[64]',
                        help='')
    parser.add_argument('--neighbors_num', nargs='?', default='[100]',
                        help='')
    parser.add_argument('--batch_size', type=int, default=1024,
                        help='')
    parser.add_argument('--regs', nargs='?', default='[1e-4]',
                        help='')
    parser.add_argument('--lr', type=float, default=0.01,
                        help='')
    parser.add_argument('--lbd', type=float, default=0.5,
                        help='')
    parser.add_argument('--pretrain_lr', type=float, default=0.0001,
                        help='')
    parser.add_argument('--model_type', nargs='?', default='hetero',
                        help='')
    parser.add_argument('--adj_type', nargs='?', default='norm',
                        help='')
    parser.add_argument('--alg_type', nargs='?', default='rw',
                        help='')
    parser.add_argument('--gpu_id', type=int, default=0,
                        help='')
    parser.add_argument('--mess_dropout', nargs='?', default='[0.1]',
                        help='')
    parser.add_argument('--Ks', nargs='?', default='[5, 10, 15, 20]',
                        help='')
    parser.add_argument('--save_flag', type=int, default=0,
                        help='')
    parser.add_argument('--test_flag', nargs='?', default='part',
                        help='')
    parser.add_argument('--sample_test_flag', nargs='?', default='full',
                        help='')
    parser.add_argument('--report', type=int, default=0,
                        help='')
    return parser.parse_args()
