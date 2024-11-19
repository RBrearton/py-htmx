<script>
  import NavBarCentre from "./NavBarCentre.svelte";
  import NavBarEnd from "./NavBarEnd.svelte";
  import NavBarStart from "./NavBarStart.svelte";

  export let lightThemeName;
  export let darkThemeName;
</script>

<div class="navbar bg-primary text-primary-content shadow">
  <NavBarStart title="Notes" />
  <NavBarCentre />
  <NavBarEnd {lightThemeName} {darkThemeName} />
</div>
