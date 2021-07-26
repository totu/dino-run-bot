# Dinorunner bot

This is a python based bot that tries to beat Chrome's dino run game.

## How?

Instead of hacking the game and controlling the dino this bot tries to read the screen as cacti and pterodactyls approach and clear these obstacles.

## Status

Best run so far has been 1042 points. Current version can not dodge the pterodactyl that requires ducking. It used to work, but in the latest refactoring I broke it. Average run currently always ends with the duck failing. As of writing this Olympics are on going and there are additional Olympic torches that trigger different Olympic themes modes. Some of which are easier than the normal run for the bot some of which are completely impossible.

## Setup

This bot is so far been coded exclusively on 13-inch MacBook Pro with Chrome taking left half of the screen. The `monitor` parameters need to be adjusted to your screen and PC separately (this is basically trial and error at this point)
To access the dino game you can use this URL `chrome://dino` or disconnect your Internet connection.

## Future

I might continue working on this if I'm bored. I might try to move on to my desktop and see if the performance is better. However I am kind a tired with fighting with the controls (I can't for the life of me figure out a way to keep the down arrow pressed.
