# Contributing Guidelines

Welcome to the MCA Students Repository for IMCC!

This repository is a shared space for coursework, programming practice, assignments, and learning activities. These guidelines help everyone collaborate using Git and GitHub while keeping contributions organized.

## 1. Repository Structure

The repository contains general documentation on `main` and shared academic work on the appropriate semester branches.

The semester branch organizes work by subject or course and then by student.

Follow the directory structure already established in the relevant semester branch. Keep your contributions inside your own student directory and the appropriate subject or course directory.

**Important:** Your Git branch and your student directory serve different purposes. A branch is a Git reference; a directory organizes files in the repository.

## 2. Branch Naming Guide

Branch names must clearly identify the student responsible for the work.

**Do not use only a subject or course name as a working branch name.** Every working branch must begin with the student's name, followed by a hyphen and a descriptive subject or task name.

| Branch purpose | Naming convention | Example |
|---|---|---|
| Student branch | `student-name` | `shailesh-parshewar` |
| Subject/course working branch | `student-name-subject-name` | `shailesh-parshewar-python` |
| Task-specific working branch | `student-name-subject-task` | `shailesh-parshewar-python-assignments` |

Use lowercase letters and hyphens to separate words. Avoid spaces and unnecessary special characters.

### Branch naming rules

- Each student should maintain one persistent student branch.
- All subject, course, or task working branches must begin with the student's name.
- Do not create generic working branches such as `python`, `dsa`, or `assignments`.
- Do not use slashes to simulate nested branches. For example, `shailesh-parshewar/python` conflicts with the existing `shailesh-parshewar` branch in Git's reference storage.
- Keep your student branch after your pull request has been merged. You will reuse it for future contributions.
- Working branches can be deleted when their work is merged and they are no longer needed.

## 3. Setting Up Your Student Branch

First, clone the repository and switch to the appropriate semester branch.

```bash
git clone <repository-url>
cd <repository-folder>

git fetch origin
git switch semester-1
git pull origin semester-1
```

Create your student branch from the semester branch:

```bash
git switch -c student-name
```

Replace `student-name` with your own name, using the naming convention above.

If you have already created your student branch, switch to it instead:

```bash
git switch student-name
```

Do not create a new student branch every time you contribute.

## 4. Creating a Working Branch

Create a separate working branch for the subject, course, or task you want to work on.

Start from your student branch:

```bash
git switch student-name
git switch -c student-name-subject-name
```

For subsequent work, create another appropriately named working branch from your student branch, or reuse an existing working branch if it is suitable and has been synchronized correctly.

**Always create working branches from your student branch, not from another subject or task branch.**

## 5. Making and Committing Changes

Work only within your assigned student directory and the appropriate subject or course directory.

Before committing, check your changes:

```bash
git status
git diff
```

Stage the relevant files and commit your work:

```bash
git add <files-or-directory>
git commit -m "Describe your changes"
```

Commit messages should be short, meaningful, and describe what changed.

Avoid vague messages such as `update`, `changes`, or `final`.

## 6. Merging Your Working Branch

Once your work is ready, merge the working branch into your student branch.

```bash
git switch student-name
git merge student-name-subject-name
```

Resolve any merge conflicts before proceeding. Test or review your changes after the merge to ensure that the resulting work is correct.

Do not merge your working branch directly into the shared semester branch.

## 7. Pushing Your Contribution

Push your student branch, not every local working branch.

```bash
git push -u origin student-name
```

If you are working through your own fork, make sure `origin` points to your fork and that the original repository is configured as `upstream`.

## 8. Creating a Pull Request

Open a pull request on GitHub with the following configuration:

- **Base repository:** The shared MCA Students Repository.
- **Base branch:** `semester-1` (or the relevant semester branch).
- **Compare branch:** Your student branch.

Before submitting the pull request, ensure that:

- Your changes are committed and pushed.
- Your files are in the correct directories.
- Your contribution does not unintentionally modify another student's work.
- Your commits contain only the intended changes.

Provide a clear title and a short description of what you have added or changed.

Wait for review and approval before considering the contribution complete.

## 9. After Your Pull Request Is Merged

**Do not delete your student branch after a pull request is merged.** It is a persistent branch intended for future coursework and contributions.

The shared semester branch now contains your merged work. Your student branch remains available for your next contribution.

Before beginning another contribution, synchronize your student branch with the latest semester branch:

```bash
git fetch origin
git switch semester-1
git pull origin semester-1

git switch student-name
git merge semester-1
```

Resolve any conflicts if they occur.

Next, create a new working branch from your updated student branch, make your changes, merge the working branch back into your student branch, and submit another pull request.

Delete an old working branch only when its work has been merged and you no longer need it.

## 10. Repository Rules

All contributors are expected to follow these rules:

- Do not push directly to protected branches.
- Do not bypass branch protections or pull request reviews.
- Do not force-push shared or protected branches.
- Do not modify another student's work without permission.
- Do not commit secrets, API keys, passwords, or other sensitive information.
- Do not add generated files, dependencies, or unrelated files unless they are required for the contribution.
- Follow the established directory structure and naming conventions.
- Keep your student branch persistent and use it for future contributions.

## 11. Common Mistakes to Avoid

- Creating a working branch with only a subject name.
- Using slashes in branch names to simulate nested branches when a student branch already exists with that prefix.
- Creating a working branch from another working branch.
- Placing files outside your own student directory.
- Opening a pull request against the wrong base branch.
- Pushing every local working branch to the shared repository.
- Deleting your student branch after a pull request is merged.
- Assuming Git branches are directories nested within other branches.

## Final Reminder

The goal of this repository is to maintain organized academic work while helping everyone develop practical Git and GitHub collaboration skills.

**Use your student branch as your persistent workspace, use clearly named working branches for individual contributions, and submit your work through pull requests.**
