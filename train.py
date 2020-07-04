import os
import sys
import subprocess as sp

train_cmd = 'LSP_train.py'
args = [
    '--model_name_or_path', 'models/medium',
    '--init_checkpoint', "models/medium/pytorch_model.bin",
    '--train_input_file', "/mnt/d/WSBBot/train.128len.db",  # file from last step
    '--eval_input_file', "/mnt/d/WSBBot/dummy_data.tsv",   # dummy test data
    '--output_dir', "/mnt/d/WSBBot/model",
    '--seed', '42',
    '--max_seq_length', '128',
    '--train_batch_size', '64',
    '--gradient_accumulation_steps', '16',
    '--eval_batch_size', '32',
    '--learning_rate', '1e-5',
    '--normalize_data', 'true',
    '--fp16', 'true',
    '--lr_schedule', 'noam',
    '--loss_scale', '0.0',
    '--no_token_id', 'true',
    '--pbar', 'true',
    '--valid_step', '2500',
    '--warmup_steps', '1000',
    '--num_optim_steps', '10000',
    # '--continue_from', '10000'
]
arg = ' '.join(args)
train_cmd = train_cmd + ' ' + arg
with open('./output.log', 'wb') as f: 
    process = sp.Popen(['python3'] + train_cmd.split(' '), stdout=sp.PIPE, stderr=sp.STDOUT, cwd=os.path.dirname(os.path.realpath(__file__)))
    for line in iter(process.stdout.readline, b''): 
        sys.stdout.write(line.decode(sys.stdout.encoding)) 
        f.write(line)
print('Done!')
