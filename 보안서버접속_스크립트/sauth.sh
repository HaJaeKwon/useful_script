#!/bin/sh
# A Shell script to connect target server through kerberos gateway server
# Wriiten by: Jaekwon.ha
# Last updated on: Nov/25/2019

[ $# -eq 0 ] && { echo "Usage: GatewayID GatewayPass TargetServerHost GoogleOTP"; exit 1; }

echo $*

GATEWAY_HOST={{GATEWAY_DOMAIN}}
GATEWAY_ID=$1
GATEWAY_PW=$2

TARGET_USER=suser
TARGET_HOST=$3

GOOGLE_OTP=$4

#SSH_COMMAND="ssh $SAUTH_GATEWAY_ID@$SAUTH_GATEWAY_DOMAIN -t 'ssh $TARGET_USER@$TARGET_HOST'"
GATEWAY="$GATEWAY_ID@$GATEWAY_HOST"
TARGET="$TARGET_USER@$TARGET_HOST"

echo "Connecting Target Server through SAuth Gateway Server"
echo "$GOOGLE_OTP"
expect -f {{PATH}}/sauth_expect.exp $GATEWAY $GATEWAY_PW $TARGET $GOOGLE_OTP

