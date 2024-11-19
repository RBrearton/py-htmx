<!-- This is the highest level component in the app. One of these is a full page. -->
<script>
  import Drawer from "./Drawer.svelte";
  import Footer from "./Footer.svelte";
  import NavBar from "./NavBar.svelte";

  const siteTitle = "Notes";
  export let pageTitle;
</script>

<NavBar lightThemeName="notes_light" darkThemeName="notes_dark" {siteTitle} />
<!-- Make the left drawer. -->
<Drawer isRightDrawer={false}>
  <!-- The left drawer content. -->
  <div slot="drawerContent">This should go in the drawer side.</div>

  <!-- Make the right drawer. -->
  <div slot="pageContent">
    <Drawer isRightDrawer={true}>
      <!-- The right drawer content. -->
      <div slot="drawerContent">The right menu</div>

      <!-- The main page content. -->
      <main slot="pageContent" class="p-10 flex flex-row justify-center">
        The main content
      </main>
    </Drawer>
  </div>
</Drawer>
<Footer />
