import argparse
import os.path
import random

best = [100, 26, 29, 45, 51, 6, 61, 82, 88, 91]
worst = [14, 15, 17, 19, 33, 59, 7, 84, 93, 99]

all = best + worst

response_prompt = os.path.abspath(os.path.join('stimuli', 'musicality', 'musical_prompt.png'))
response_confirm_yes = os.path.abspath(os.path.join('stimuli', 'musicality', 'musical_response_yes.png'))
response_confirm_no = os.path.abspath(os.path.join('stimuli', 'musicality', 'musical_response_no.png'))

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Create a musicality experiment")

  parser.add_argument("--out", dest="outpath", help="Output experiment definition file", type=str, required=True)
  parser.add_argument("--seed", dest="seed", help="Random seed", type=int, required=True)

  args = parser.parse_args()
  random.seed(args.seed)

  ncycles = 5
  reflection_time = 3.0
  reflection_marker = 2
  response_marker = 3
  play_start = 0
  play_end = 5

  confirm_duration = .5
  yes_keycode = 37 # left arrow
  no_keycode = 39  # right arrow

  post_confirm_duration = 1

  response_line = "RESPONSE %d %s %f %d %s %d %s\n" % (response_marker, response_prompt, 
      confirm_duration, yes_keycode, response_confirm_yes, no_keycode, response_confirm_no)
  post_confirm_line = "BLANK 2 %f\n" % post_confirm_duration

  with open(args.outpath, 'w') as f:
    f.write("BLANK 1 .5\n")
    f.write("BLANK 1 .5\n")
    f.write("BLANK 1 .5\n")
    f.write("BLANK 1 .5\n")
    f.write("BLANK 1 .5\n")
    f.write("BLANK 2 5\n")

    for ci in range(ncycles):
      random.shuffle(all)

      for song_index in all:
        path = os.path.abspath(os.path.join('stimuli/musicality/wavs/D%d.wav' % song_index))
        f.write("SOUND %d %f %f %s\n" % (100 + song_index, play_start, play_end, path))
        f.write("BLANK %d %f\n" % (reflection_marker, reflection_time))
        f.write(response_line)
        f.write(post_confirm_line)

    




