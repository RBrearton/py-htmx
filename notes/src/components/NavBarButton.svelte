<script>
  import NavBarHeading from "./NavBarHeading.svelte";

  // Take one prop for the text, another for the route.
  export let text;
  export let route;
</script>

<a class="btn btn-ghost" href={route}>
  <NavBarHeading title={text} isPadded={false} />
</a>
