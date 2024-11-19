<!-- Router.svelte -->
<script lang="ts">
  import { onMount } from "svelte";
  import { Router, Route, Link } from "svelte-routing";
  import NotesPage from "./NotesPage.svelte";

  interface RouteModel {
    name: string;
    path: string;
  }
  let routes: RouteModel[] = [];

  onMount(async () => {
    const response = await fetch("/api/routes");
    routes = await response.json();
  });
</script>

<Router>
  <nav>
    {#each routes as route}
      <Link to={route.path}>{route.name}</Link>
    {/each}
  </nav>
  {#each routes as route}
    <Route path={route.path} component={NotesPage} props={{ pageTitle: route.name }} />
  {/each}
</Router>
