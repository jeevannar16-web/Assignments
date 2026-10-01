# Assignments

All my class assignments and practice work in one place, collected from the
individual subject repos that used to live separately.

| Folder | Subject | Language | Original repo |
|---|---|---|---|
| [`branching/`](branching/) | Git branching practice — branches, merges, stash, cherry-pick | — | `branching` |
| [`c-plus-plus/`](c-plus-plus/) | Class 10 C++ labwork, exam papers, chapter exercises | C++ | `c-plus-plus` |
| [`java/`](java/) | Class 11 Java — basics through classes and objects | Java | `Java-class-11-` |
| [`python/`](python/) | Python fundamentals — basics, strings, loops, conditionals, OOP | Python | `Python` |
| [`ojt/`](ojt/) | On-the-job training notes and practice files | — | `Jeevan_Ojt` |

Every folder kept its original commit history, so `git log` inside any of them
still shows the individual work as it was written.

## Layout

```
Assignments/
├── README.md
├── .gitignore
├── branching/       git exercises
├── c-plus-plus/     C++ coursework
├── java/            Java coursework
├── python/          Python coursework
└── ojt/             OJT notes
```

## Notes

- Compiled Windows executables (`*.exe`) were committed in the original C++
  repo and are left in place so nothing is lost. They are ignored going
  forward, so rebuild locally with a C++ compiler.
- `.class` files, IDE folders and OS junk are ignored.