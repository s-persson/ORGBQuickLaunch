from openrgb import OpenRGBClient
cli = OpenRGBClient()
with open('profile.txt') as p:
    cli.load_profile(p.readline())