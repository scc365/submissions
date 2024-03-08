# Submission Counter

Display the number of submissions to a moodle submission point in the terminal.

## Build

Build the docker image locally:

```bash
docker build --rm -t submissions:latest -f Dockerfile .
```

## Run

Run the docker image, giving the 3 expected commands:
  - **Assignment ID**: The ID for the assignment's moodle page typically found
    as a param in the submission point's URL. For example, the submission page
    `https://modules.lancaster.ac.uk/mod/assign/view.php?id=123456` would mean
    the relevant ID value is `123456`.
  - **Moodle Cookie**: Your session cookie for moodle to be extracted from a web
    browser where you are signed into moodle (specifically to an account where
    you have permission to see the associated submission page). The value for
    this should be the cookie value for the key
    `cosign-https-modules.lancaster.ac.uk`.
  - **Figlet Font**: The font to use from `figlet` when displaying the output.

```bash
docker run --rm -it submissions:latest <id> <cookie> <font>
```

> For live data, just use the above command prefixed with `watch -t` (by
> default this is updated every 2 seconds).

---

This is all super jank. If you are reading this, too late, fixing this is your
responsibility now.
