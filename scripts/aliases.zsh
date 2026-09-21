# beau-bou — Shopify theme aliases
# Install:  echo 'source ~/LocalStorm/Workspace/DevProjects/GitHub/beau-bou/scripts/aliases.zsh' >> ~/.zshrc
# (or stow it from your dotfiles repo — this file has no side effects on source)

export BEAU_BOU_DIR="${BEAU_BOU_DIR:-$HOME/LocalStorm/Workspace/DevProjects/GitHub/beau-bou}"

bb()           { cd "$BEAU_BOU_DIR" || return 1; }
bb-dev()       { bb && shopify theme dev -e dev "$@"; }              # hot-reload against Amber's build store
bb-dev-client(){ bb && shopify theme dev -e client "$@"; }           # hot-reload against Michele's store
bb-check()     { bb && shopify theme check "$@"; }
bb-push-dev()  { bb && shopify theme push -e dev --unpublished "$@"; }
bb-push()      { bb && shopify theme push -e client --unpublished "$@"; }  # never auto-publishes; publish from admin
bb-pull()      { bb && shopify theme pull -e client --only config/settings_data.json --only 'templates/*.json' --only 'sections/*.json'; }
bb-zip()       { bb && shopify theme package && ls -1t *.zip | head -1; }   # zip for manual upload in Themes > Add theme
bb-preview()   { bb && open docs/preview/index.html; }

# Looks — hero runway cutouts + shop-this-look metaobjects (docs/looks.md)
bb-cutouts()   { bb && python3 scripts/cutouts.py "$@"; }               # styled photos → transparent runway cutouts + docs/looks/looks.json
bb-looks-seed(){ bb && node scripts/looks/seed-looks.ts "$@"; }         # needs SHOPIFY_STORE + SHOPIFY_ADMIN_TOKEN; --dry / --skip-files / --only <handle>
bb-looks-client(){ SHOPIFY_STORE=v0m0hb-x3 bb-looks-seed "$@"; }        # Michele's store (token still from env)

# One-shot: create Michele's empty collections in whichever store you're logged into (needs `shopify` auth + Admin API scope)
# Prefer the Shopify MCP / admin UI; this is a fallback list to paste.
bb-collections(){ cat "$BEAU_BOU_DIR/docs/collections.md"; }
