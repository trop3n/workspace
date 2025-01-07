{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.chromium
    pkgs.chromedriver
    pkgs.python3
    pkgs.python3Packages.selenium
    pkgs.python3Packages.webdriver-manager
  ];

  # Fix for ChromeDriver not finding libraries
  shellHook = ''
    export CHROME_PATH="${pkgs.chromium}/bin/chromium"
    export CHROME_DRIVER_PATH="${pkgs.chromedriver}/bin/chromedriver"
  '';
}