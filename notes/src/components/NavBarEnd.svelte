<script>
  import GithubLink from "./GithubLink.svelte";
  import SearchBar from "./SearchBar.svelte";
  import ThemeSelector from "./ThemeSelector.svelte";
</script>

<div class="navbar-end">
  <ThemeSelector />
  <SearchBar placeholder="Search" />
  <GithubLink link="https://github.com/rbrearton/py-htmx" />
</div>
