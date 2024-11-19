<script>
  import GithubLink from "./GithubLink.svelte";
  import SearchBar from "./SearchBar.svelte";
  import ThemeSelector from "./ThemeSelector.svelte";

  export let lightThemeName;
  export let darkThemeName;
</script>

<div class="navbar-end">
  <ThemeSelector {lightThemeName} {darkThemeName} />
  <SearchBar placeholder="Search" />
  <GithubLink link="https://github.com/rbrearton/py-htmx" />
</div>
