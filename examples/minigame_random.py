"""
   Copyright 2017 Islam Elnabarawy

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import argparse

from examples.base_example import BaseExample

__author__ = 'Islam Elnabarawy'
__description__ = 'Run an example doing random actions on a minigame environment.'


class MinigameRandom(BaseExample):
    def __init__(self, env_name, visualize=False, step_mul=None) -> None:
        super().__init__(env_name, visualize, step_mul)

    def get_action(self, env, obs):
        return env.action_space.sample()


def main():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('--env-name', type=str, required=True,
                        help='the name of the minigame environment')
    parser.add_argument('--visualize', type=bool, default=False,
                        help='show the pysc2 visualizer')
    parser.add_argument('--num-episodes', type=int, default=10,
                        help='number of episodes to run')
    parser.add_argument('--step-mul', type=int, default=None,
                        help='number of game steps to take per turn')
    args = parser.parse_args()

    example = MinigameRandom(args.env_name, args.visualize, args.step_mul)
    rewards = example.run(args.num_episodes)
    print('Total reward: {}'.format(rewards.sum()))
    print('Average reward: {} +/- {}'.format(rewards.mean(), rewards.std()))
    print('Minimum reward: {}'.format(rewards.min()))
    print('Maximum reward: {}'.format(rewards.max()))


if __name__ == "__main__":
    main()
