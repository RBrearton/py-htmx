<script>
  import NavBarCentre from "./NavBarCentre.svelte";
  import NavBarEnd from "./NavBarEnd.svelte";
  import NavBarStart from "./NavBarStart.svelte";

  export let lightThemeName;
  export let darkThemeName;
  export let siteTitle;
</script>

<div class="navbar bg-primary text-primary-content shadow">
  <NavBarStart title={siteTitle} />
  <NavBarCentre />
  <NavBarEnd {lightThemeName} {darkThemeName} />
</div>
