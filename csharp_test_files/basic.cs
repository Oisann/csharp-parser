import UnityEngine;
import System.Collections;

namespace TBA.Game {
    public class Controller : MonoBehaviour {
        public int startTime = 0;
        [SerializeField]
        private float numbers = 100f;
        private Vector3 pos = Vector3.zero;
        [SerializeField] private float abc = 10f;

        private void Start() {
            var test = "A string 'with//another fake inside' \"and something // haha \" a fake //comment"; //and a real comment afterwards
            var test2 = 'mamma "mia" // pappa'; // comment after again
            // Single-line comment
            SetupController(test); // another comment at the end
        }

        private void Update() {
            /*
                Multi-line comment on every frame
             */Debug.Log("/* end of multiline comment */");
            Jump();
        }

        internal void SetupController(string str) {
            /* Multi-line comment on a single line */
            Debug.Log(str);
        }

        void Jump()
        {
            var magicNumber/*_old */ = magic(0,/* 11 */ 10);
            print(/* test comment inside something else */magicNumber);
        }

        internal int magic ( int min,
                            int max ) {
            return 9;
        }
    }
}