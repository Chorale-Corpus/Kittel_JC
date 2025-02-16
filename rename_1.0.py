import os, re
import subprocess
from pprint import pprint


def make_new_fname(name, ext):
    """Transforms an old file name into a new one."""
    return f"0{name}{ext}"

def make_renaming_dict(path, regex, full_paths=True) -> dict:
    """Go through all subdirectories of path, collect all file names that match the regex,
    and return a dictionary that maps them to their new file names according to make_new_fname.
    """
    renaming = {}

    for subdir, dirs, files in os.walk(path):
        for old_fname in sorted(files):
            name, ext = os.path.splitext(old_fname)
            if re.match(regex, name):
                new_fname = make_new_fname(name, ext)
                if full_paths:
                    old_path = os.path.join(subdir, old_fname)
                    new_path = os.path.join(subdir, new_fname)
                    renaming[old_path] = new_path
                else:
                    if old_fname in renaming:
                        print(f"Warning: {old_fname} already in renaming dict.")
                    else:
                        renaming[old_fname] = new_fname
    return renaming





def rename_files(renaming_dict, use_git=False):
    for old_path, new_path in renaming_dict.items():
        try:
            if use_git:
                subprocess.call(["git", "mv", old_path, new_path])
            else:
                os.rename(old_path, new_path)
            print(f"Renamed {old_path}  =>  {new_path}")
        except Exception as e:
            print(f"Renaming {old_path!r} failed with {e!r}")


if __name__ == "__main__":
    path = os.path.abspath('MultibassChorales/mxl')
    print(f"CWD: {path}")
    no_leading_0_regex = r"^\d{2}_"
    fnames_to_rename = make_renaming_dict(path, no_leading_0_regex, full_paths=False)
    pprint(fnames_to_rename)
    # renaming_dict = make_renaming_dict(path, no_leading_0_regex, full_paths=True)
    # rename_files(renaming_dict, use_git=True)