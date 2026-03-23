#!/usr/bin/env bash

set -e

BASE_DIR="static/icons"
OS_DIR="$BASE_DIR/os"
BROWSER_DIR="$BASE_DIR/browser"

mkdir -p "$OS_DIR" "$BROWSER_DIR"

echo "⬇️  Downloading OS icons..."

curl -L -o "$OS_DIR/macos.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/apple.svg

curl -L -o "$OS_DIR/windows.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/windows.svg

curl -L -o "$OS_DIR/linux.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/linux.svg

curl -L -o "$OS_DIR/android.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/android.svg

curl -L -o "$OS_DIR/ios.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/apple.svg


echo "⬇  Downloading browser icons..."

curl -L -o "$BROWSER_DIR/chrome.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/googlechrome.svg

curl -L -o "$BROWSER_DIR/firefox.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/firefoxbrowser.svg

curl -L -o "$BROWSER_DIR/safari.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/safari.svg

curl -L -o "$BROWSER_DIR/edge.svg" \
  https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/microsoftedge.svg

echo "All icons downloaded successfully!"
