{
  description = "python 3.12, django 5.0.1";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
	let
	  system = "x86_64-linux";
	  pkgs = import nixpkgs { inherit system; };
	in {
	  devShells.${system}.default = pkgs.mkShell {
	    packages = [
	      # essential packages
	      pkgs.python312
	      pkgs.python312Packages.pip
	      pkgs.python312Packages.virtualenv

	      # project-specific libraries

	      # runtime libraries
	      pkgs.glib
	      pkgs.gtk3
	      pkgs.SDL2
	      pkgs.libpulseaudio
	    ];

	    shellHook = ''
	      if [ ! -d .venv ]; then
	        python3 -m venv .venv
	      fi

	      source .venv/bin/activate
	    '';
	  };
	};
}
