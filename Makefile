GITHUB_URL      = ""
PUBLIC_BRANCHES = "master"
GIT_ORIGIN_URL  = $(shell git config remotes.origin.url)

test:
	python setup.py test

# Github Commands
# ===============

github-init:
	[ -n "$(GIT_ORIGIN_URL)" ] || git add remote origin "$(GITHUB_URL)"
	[ "$(GITHUB_URL)" = "$(GIT_ORIGIN_URL)" ] || { echo "ERROR: git origin url = $(GIT_ORIGIN_URL)"; exit 1 }

github-publish: github-init
	for branch in $(PUBLIC_BRANCHES); do\
		git push origin $$branch;\
	done

# PyPI Commands
# =============

pypi-publish:
	python setup.py sdist upload

pypi-register:
	python setup.py register

.PHONY: test github-init github-publish pypi-publish pypi-register
