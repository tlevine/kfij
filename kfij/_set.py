import logging
import os

class Set:
    '''
    Persist a set-like structure to a file.
    The contents of the set must be str or bytes.
    '''
    def __init__(self, filename, binary_mode = False):
        '''
        :param str filename: File at which to save state
        :param bool binary_mode: Whether the file should be opened in binary mode
            and, in turn, whether you are going to add bytes or str to the set
        '''
        b = 'b' if binary_mode else ''

        if os.path.exists(filename):
            with open(filename, 'r') as fp:
                original_data = set(line.rstrip('\r\n') for line in fp)
        else:
            with open(filename, 'w') as fp:
                fp.write('')
            original_keys_to_skip = set()

        keys_to_skip = set(original_keys_to_skip)
        for x in xs:
            key, _ = x

            # Validate key
            if not isinstance(key, str) or '\r' in key or '\n' in key:
                raise NotImplementedError('Can\'t handle this sort of key')

            # Filter
            if key in keys_to_skip:
                logger.debug('Skipping key "%s" from %s' % (key, xs))
            else:
                keys_to_skip.add(key)
                yield x

        with open(filename, 'a') as fp:
            for key in keys_to_skip - original_keys_to_skip:
                fp.write(key + '\n')
