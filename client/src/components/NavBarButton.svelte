<script>
  import { Link } from "svelte-routing";
  import NavBarHeading from "./NavBarHeading.svelte";

  // Take one prop for the text, another for the route.
  export let text;
  export let route;
</script>

<Link class="btn btn-ghost" to={route}>
  <NavBarHeading title={text} isPadded={false} />
</Link>
