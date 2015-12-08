import urllib2
import boto


response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
key = response.read().split(':')

key_id = key[0]
key_secret = key[1]

print 'ID:',key_id
print 'Access:', key_secret
print boto.Version



