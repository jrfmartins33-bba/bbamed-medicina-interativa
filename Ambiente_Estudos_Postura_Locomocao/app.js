const modules = [
  {
    id: "base",
    title: "1. Base do sistema motor",
    time: "12 min",
    slides: [2, 3],
    goal: "Entender o movimento como uma cadeia integrada: decisão, ajuste, execução e feedback.",
    summary:
      "Movimento não é apenas músculo contraindo. Ele depende de cérebro, medula, músculos e sentidos trabalhando de forma coordenada. O córtex decide e planeja, o tronco encefálico ajusta comandos automáticos, a medula organiza a saída final e os músculos executam.",
    concepts: [
      ["Córtex", "Decide, planeja e comanda movimentos voluntários, especialmente movimentos conscientes e finos."],
      ["Tronco encefálico", "Ajusta tônus, reflexos, equilíbrio e respostas rápidas para manter a postura."],
      ["Medula", "Recebe comandos descendentes e envia a ordem final aos músculos por neurônios motores inferiores."],
      ["Feedback sensorial", "Informa posição, movimento e erro, permitindo correções imediatas."]
    ],
    exam: "Se a pergunta falar em movimento voluntário fino, pense em córtex e trato corticoespinal. Se falar em ajuste postural automático, pense em tronco, vias extrapiramidais e integração sensorial."
  },
  {
    id: "cortex",
    title: "2. Córtex motor e áreas associadas",
    time: "16 min",
    slides: [4, 5, 6, 7],
    sceneLinks: [
      { label: "Cena 03 — Homúnculo Sensorial", href: "cena03_homunculo_sensorial_1.html" }
    ],
    goal: "Diferenciar córtex motor primário, área pré-motora e área suplementar.",
    summary:
      "O córtex motor fica no giro pré-central, no lobo frontal. Ele inicia movimentos voluntários. A representação corporal é somatotópica: cada região corporal tem uma área cortical relacionada. Áreas associadas ajudam a preparar movimentos com base em estímulos externos e sequências aprendidas.",
    concepts: [
      ["Córtex motor primário", "Principal origem de comandos voluntários; envia fibras para o trato corticoespinal."],
      ["Homúnculo motor", "Mapa corporal no córtex. Regiões que exigem precisão, como mãos e face, ocupam mais área."],
      ["Área pré-motora", "Planeja movimentos guiados por estímulos externos, como visão e ambiente."],
      ["Área suplementar", "Organiza sequências de movimentos aprendidos e repetidos."]
    ],
    exam: "A mão e a face são grandes no homúnculo porque precisam de controle fino, não porque sejam maiores no corpo."
  },
  {
    id: "corticoespinal",
    title: "3. Trato corticoespinal",
    time: "18 min",
    slides: [8, 9, 10, 12],
    sceneLinks: [
      { label: "Cena 04 — Trato Corticoespinhal", href: "cena04_trato_corticoespinhal.html" }
    ],
    goal: "Seguir a via voluntária do córtex até o músculo.",
    summary:
      "O trato corticoespinal é a via voluntária mais importante para o controle consciente dos movimentos. Ele nasce principalmente no córtex motor primário, desce pelo tronco encefálico, cruza em grande parte na decussação das pirâmides e chega à medula, onde influencia interneurônios e neurônios motores inferiores.",
    concepts: [
      ["Origem", "Córtex motor, com forte participação do córtex motor primário."],
      ["Trajeto", "Desce pelo encéfalo e tronco encefálico até a medula espinhal."],
      ["Decussação", "Muitas fibras cruzam no bulbo, explicando controle contralateral."],
      ["Função", "Permite movimentos voluntários precisos, especialmente de músculos distais."]
    ],
    exam: "Lesão acima da decussação tende a afetar o lado oposto do corpo. Lesão abaixo da decussação tende a afetar o mesmo lado."
  },
  {
    id: "tronco",
    title: "4. Tronco encefálico e vias extrapiramidais",
    time: "18 min",
    slides: [11, 13, 14],
    sceneLinks: [
      { label: "Cena 05 — Tronco Encefálico", href: "cena05_HOTSPOTS_3.html" },
      { label: "Cena 06 — Três Andares do Tronco Encefálico", href: "cena06_tres_andares_tronco_encefalico.html" }
    ],
    goal: "Entender o controle automático que sustenta postura e locomoção.",
    summary:
      "O tronco encefálico regula funções motoras básicas sem necessidade de consciência. Ele integra córtex, cerebelo e medula, mantém tônus muscular, coordena reflexos e participa do equilíbrio. As vias extrapiramidais são essenciais para movimentos automáticos e ajustes posturais.",
    concepts: [
      ["Vestibuloespinal", "Usa informação do ouvido interno para ajustar postura e equilíbrio."],
      ["Reticuloespinal", "Regula tônus muscular, movimentos automáticos e respostas posturais."],
      ["Rubroespinal", "Ajuda no controle de músculos flexores, principalmente de membros superiores."],
      ["Núcleos motores", "Mesencéfalo, ponte e bulbo abrigam núcleos que integram funções visuais, auditivas, faciais, viscerais e respiratórias."]
    ],
    exam: "Vias extrapiramidais não são o centro do movimento fino consciente; elas dão base, ajuste e automatismo ao movimento."
  },
  {
    id: "postura",
    title: "5. Controle da postura e integração sensorial",
    time: "20 min",
    slides: [15, 16],
    sceneLinks: [
      { label: "Cena 07 — Controle da Postura e Integração Sensorial", href: "cena07_controle_postura_integracao_sensorial.html" }
    ],
    goal: "Compreender como o corpo se mantém estável contra a gravidade.",
    summary:
      "Postura é estabilidade ativa. Reflexos e ajustes automáticos mantêm o corpo contra a gravidade. Propriocepção, sistema vestibular e visão se combinam para orientar o corpo no espaço. Antes do movimento, há ajustes antecipatórios; quando há desequilíbrio, ajustes compensatórios corrigem rapidamente.",
    concepts: [
      ["Propriocepção", "Informa posição e movimento de articulações e músculos."],
      ["Vestibular", "Detecta posição da cabeça e aceleração, ajudando equilíbrio."],
      ["Visão", "Orienta o corpo no espaço e ajuda na direção do movimento."],
      ["Ajustes posturais", "Antecipatórios preparam o corpo; compensatórios corrigem perdas de equilíbrio."]
    ],
    exam: "Postura não é passividade. É um conjunto de ajustes automáticos que permite ficar de pé, alcançar objetos, caminhar e corrigir perturbações."
  },
  {
    id: "clinica",
    title: "6. Síndromes neurológicas",
    time: "22 min",
    slides: [17, 18, 19, 20, 21],
    goal: "Comparar NMS, NMI e alterações cerebelares.",
    summary:
      "O neurônio motor superior comanda de cima e modula o neurônio motor inferior. Quando o NMS é lesado, perde-se controle inibitório, gerando espasticidade, hiperreflexia e Babinski. Quando o NMI é lesado, a ativação muscular falha, com fraqueza, hipotonia, hiporreflexia e atrofia. Lesão cerebelar compromete coordenação.",
    concepts: [
      ["Síndrome NMS", "Espasticidade, hiperreflexia, Babinski e fraqueza central."],
      ["Síndrome NMI", "Fraqueza por falha de ativação, hipotonia, hiporreflexia e atrofia."],
      ["Cerebelar", "Ataxia, dismetria, tremor de intenção e marcha instável."],
      ["Exemplos NMS", "AVC, paralisia cerebral, esclerose múltipla, ELA, esclerose lateral primária e paraplegia espástica hereditária."]
    ],
    exam: "A comparação NMS versus NMI costuma ser ponto de prova: NMS aumenta reflexos e tônus; NMI reduz reflexos e tônus."
  }
];

const slides = [
  ["page01.png", "Capa", "Aula de Postura e Locomoção, ministrada pelo Prof. Lucas de Queiroz Chaves.", false],
  ["page02.png", "Introdução ao sistema motor", "Movimento integra cérebro, medula, músculos e sentidos. Córtex decide, tronco ajusta e medula executa.", true],
  ["page03.png", "Organização do sistema motor", "Neurônio motor superior nasce no encéfalo e leva ordem à medula; neurônio motor inferior sai da medula para o músculo.", true],
  ["page04.png", "Córtex motor", "Giro pré-central no lobo frontal; inicia movimentos voluntários e permite ações conscientes como pegar objetos e caminhar.", true],
  ["page05.png", "Córtex motor e sensorial", "Imagem das faixas cortical motora e sensorial. Ajuda a visualizar a somatotopia.", false],
  ["page06.png", "Homúnculo cortical", "Representação corporal distorcida: mãos, face e boca aparecem maiores pela necessidade de precisão.", false],
  ["page07.png", "Áreas motoras associadas", "Área pré-motora planeja com estímulos externos; área suplementar organiza movimentos aprendidos.", true],
  ["page08.png", "Feixe corticoespinal", "Via voluntária mais importante para controle consciente, com forte papel em movimentos finos.", true],
  ["page09.png", "Organização corticoespinal", "O trato surge principalmente do córtex motor primário, desce até a medula e age direta ou indiretamente por interneurônios.", true],
  ["page10.png", "Diagrama do trato corticoespinal", "Mostra origem cortical, descida pelo tronco, decussação e chegada à medula.", false],
  ["page11.png", "Tronco encefálico", "Controle automático de funções motoras básicas, tônus, reflexos e equilíbrio.", true],
  ["page12.png", "Vias descendentes", "Comparação visual entre trato corticoespinal lateral e via rubroespinal.", false],
  ["page13.png", "Vias extrapiramidais", "Vestibuloespinal, reticuloespinal e rubroespinal ajustam postura, tônus e movimentos automáticos.", true],
  ["page14.png", "Núcleos motores do tronco", "Mesencéfalo, ponte e bulbo integram funções motoras, viscerais, oculares e posturais.", false],
  ["page15.png", "Controle da postura", "Reflexos e ajustes automáticos mantêm estabilidade contra a gravidade.", true],
  ["page16.png", "Integração sensorial", "Propriocepção, vestibular e visão informam posição, movimento e erro para correções rápidas.", true],
  ["page17.png", "NMS e NMI", "Neurônio motor superior conduz comando até a medula; neurônio motor inferior leva a ordem final ao músculo.", false],
  ["page18.png", "Síndrome do NMS", "Espasticidade, hiperreflexia, Babinski e fraqueza central por perda de controle inibitório.", true],
  ["page19.png", "Doenças do NMS", "Exemplos: AVC, paralisia cerebral, esclerose múltipla, ELA, esclerose lateral primária e paraplegia espástica hereditária.", false],
  ["page20.png", "Síndrome do NMI", "Fraqueza, hipotonia, hiporreflexia e atrofia por falha de ativação muscular.", true],
  ["page21.png", "Síndromes cerebelares", "Ataxia, dismetria, tremor de intenção e marcha instável por falha de coordenação.", true]
].map((item, index) => ({
  number: index + 1,
  src: `../page_images/${item[0]}`,
  title: item[1],
  note: item[2],
  rotate: item[3]
}));

const flashcards = [
  ["Qual é a ideia central do sistema motor?", "Movimento resulta da integração entre cérebro, medula, músculos e sentidos."],
  ["O que o córtex faz no movimento?", "Decide, planeja e envia comandos motores voluntários."],
  ["O que o tronco encefálico ajusta?", "Tônus, postura, equilíbrio, reflexos e respostas motoras automáticas."],
  ["Qual é o papel da medula?", "Receber comandos descendentes e enviar a ordem final aos músculos."],
  ["Onde fica o córtex motor primário?", "No giro pré-central, no lobo frontal."],
  ["Por que mãos e face são grandes no homúnculo?", "Porque exigem controle fino e grande precisão motora."],
  ["O que a área pré-motora faz?", "Planeja movimentos guiados por estímulos externos, como visão e ambiente."],
  ["O que a área suplementar faz?", "Organiza sequências de movimentos aprendidos e automatizados."],
  ["Qual é a principal função do trato corticoespinal?", "Controlar movimentos voluntários conscientes, principalmente finos e distais."],
  ["O que é decussação das pirâmides?", "Cruzamento de muitas fibras corticoespinais no bulbo."],
  ["Por que uma lesão cortical direita pode afetar o lado esquerdo?", "Porque muitas fibras corticoespinais cruzam antes de chegar à medula."],
  ["O que são vias extrapiramidais?", "Vias motoras automáticas que regulam postura, tônus, equilíbrio e movimentos não conscientes."],
  ["Função da via vestibuloespinal?", "Ajustar postura e equilíbrio com base no ouvido interno."],
  ["Função da via reticuloespinal?", "Regular tônus, postura e movimentos automáticos."],
  ["Função da via rubroespinal?", "Participar do controle de músculos flexores, especialmente nos membros superiores."],
  ["Quais sistemas alimentam a integração sensorial?", "Propriocepção, sistema vestibular e visão."],
  ["O que são ajustes antecipatórios?", "Preparações posturais que acontecem antes do movimento."],
  ["O que são ajustes compensatórios?", "Correções rápidas após perturbação ou perda de equilíbrio."],
  ["Sinais típicos da síndrome do NMS?", "Espasticidade, hiperreflexia, Babinski e fraqueza central."],
  ["Sinais típicos da síndrome do NMI?", "Fraqueza, hipotonia, hiporreflexia e atrofia."],
  ["Sinais típicos de síndrome cerebelar?", "Ataxia, dismetria, tremor de intenção e marcha instável."],
  ["Qual síndrome tem hiperreflexia?", "Síndrome do neurônio motor superior."],
  ["Qual síndrome tem hiporreflexia?", "Síndrome do neurônio motor inferior."],
  ["Qual estrutura corrige movimento e coordenação?", "Cerebelo, em conjunto com feedback sensorial e vias motoras."]
].map((item, index) => ({ id: `card-${index}`, q: item[0], a: item[1] }));

const quiz = [
  {
    q: "Um estudante escreve: 'movimento é só contração muscular'. Qual correção está mais completa?",
    options: [
      "Movimento depende de cérebro, medula, músculos e feedback sensorial.",
      "Movimento depende apenas de reflexos medulares.",
      "Movimento depende apenas da visão.",
      "Movimento depende apenas do cerebelo."
    ],
    answer: 0,
    why: "A aula apresenta movimento como integração entre centros nervosos, vias motoras, músculos e sentidos."
  },
  {
    q: "Qual região cortical é a principal origem dos comandos voluntários motores?",
    options: ["Córtex motor primário", "Hipocampo", "Córtex auditivo", "Tálamo visual"],
    answer: 0,
    why: "O córtex motor primário, no giro pré-central, é a principal área voluntária motora."
  },
  {
    q: "A área pré-motora é mais associada a:",
    options: [
      "Planejar movimentos com base em estímulos externos.",
      "Produzir reflexo patelar isolado.",
      "Regular frequência respiratória.",
      "Ativar diretamente todos os músculos sem medula."
    ],
    answer: 0,
    why: "A área pré-motora planeja ações usando informações externas, como visão."
  },
  {
    q: "A área motora suplementar é fundamental para:",
    options: [
      "Sequências de movimentos aprendidos.",
      "Detecção de sons.",
      "Contração isolada sem aprendizagem.",
      "Controle exclusivo da pupila."
    ],
    answer: 0,
    why: "Ela organiza sequências, especialmente movimentos aprendidos e repetidos."
  },
  {
    q: "Qual via está mais ligada a movimentos voluntários finos?",
    options: ["Corticoespinal", "Vestibuloespinal", "Reticuloespinal", "Via olfatória"],
    answer: 0,
    why: "O trato corticoespinal é a via voluntária principal para movimentos finos."
  },
  {
    q: "O cruzamento de muitas fibras corticoespinais ocorre principalmente:",
    options: ["No bulbo, na decussação das pirâmides.", "No cerebelo.", "Na retina.", "No músculo."],
    answer: 0,
    why: "A decussação das pirâmides no bulbo explica o controle contralateral de muitos movimentos."
  },
  {
    q: "Qual alternativa resume melhor as vias extrapiramidais?",
    options: [
      "Ajustam postura, tônus, equilíbrio e movimentos automáticos.",
      "São responsáveis apenas por movimentos finos dos dedos.",
      "Substituem totalmente o córtex motor.",
      "Atuam apenas na audição."
    ],
    answer: 0,
    why: "As vias extrapiramidais dão base automática para postura e locomoção."
  },
  {
    q: "A via vestibuloespinal usa informação principalmente de qual sistema?",
    options: ["Ouvido interno", "Paladar", "Olfato", "Pele da face"],
    answer: 0,
    why: "Ela usa dados vestibulares para equilíbrio e postura."
  },
  {
    q: "Qual conjunto é essencial para integração sensorial postural?",
    options: [
      "Propriocepção, vestibular e visão.",
      "Olfato, paladar e audição.",
      "Memória, linguagem e emoção.",
      "Pele, fígado e rim."
    ],
    answer: 0,
    why: "Esses três sistemas informam posição, aceleração, orientação e correções do movimento."
  },
  {
    q: "O corpo se prepara para levantar um braço sem cair. Isso é exemplo de:",
    options: ["Ajuste antecipatório", "Atrofia", "Hiporreflexia", "Dismetria"],
    answer: 0,
    why: "Ajustes antecipatórios preparam a postura antes do movimento."
  },
  {
    q: "A correção rápida depois de escorregar é exemplo de:",
    options: ["Ajuste compensatório", "Somatotopia", "Atrofia muscular", "Decussação"],
    answer: 0,
    why: "Ajustes compensatórios corrigem perturbações após ameaça ao equilíbrio."
  },
  {
    q: "Qual achado aponta para síndrome do neurônio motor superior?",
    options: ["Espasticidade e hiperreflexia", "Hipotonia e atrofia", "Perda de volume por desuso apenas", "Tremor de intenção isolado"],
    answer: 0,
    why: "NMS perde modulação inibitória, favorecendo aumento de tônus e reflexos."
  },
  {
    q: "Qual achado aponta para síndrome do neurônio motor inferior?",
    options: ["Hipotonia, hiporreflexia e atrofia", "Babinski e espasticidade", "Somente alteração visual", "Apenas hiperreflexia"],
    answer: 0,
    why: "NMI lesionado compromete a ativação final do músculo."
  },
  {
    q: "Babinski é mais associado a:",
    options: ["Lesão de neurônio motor superior", "Lesão isolada de neurônio motor inferior", "Doença renal", "Alteração vestibular simples"],
    answer: 0,
    why: "Babinski é reflexo patológico típico de acometimento piramidal/NMS."
  },
  {
    q: "Ataxia, dismetria e tremor de intenção sugerem alteração:",
    options: ["Cerebelar", "Exclusivamente corticoespinal", "Exclusivamente muscular", "Do nervo olfatório"],
    answer: 0,
    why: "Esses sinais apontam falha de coordenação, típica do cerebelo."
  }
];

const cases = [
  {
    title: "Caso 1",
    text: "Paciente com rigidez, reflexos exaltados e sinal de Babinski após AVC.",
    answer: "NMS",
    why: "AVC pode atingir vias motoras superiores; hiperreflexia e Babinski apontam NMS."
  },
  {
    title: "Caso 2",
    text: "Paciente com fraqueza, músculo flácido, reflexos diminuídos e perda de volume muscular.",
    answer: "NMI",
    why: "Hipotonia, hiporreflexia e atrofia indicam falha de ativação pelo neurônio motor inferior."
  },
  {
    title: "Caso 3",
    text: "Paciente erra a distância ao pegar objetos e caminha com base alargada.",
    answer: "Cerebelar",
    why: "Dismetria, ataxia e marcha instável sugerem alteração cerebelar."
  },
  {
    title: "Caso 4",
    text: "Ao fechar os olhos, a pessoa perde muita estabilidade porque depende de pistas visuais.",
    answer: "Sensorial",
    why: "A postura usa visão, vestibular e propriocepção. Retirar uma fonte pode expor dependência das outras."
  },
  {
    title: "Caso 5",
    text: "Movimento voluntário fino dos dedos fica prejudicado, com suspeita de lesão em via descendente piramidal.",
    answer: "Corticoespinal",
    why: "A via corticoespinal é central para movimentos voluntários finos, especialmente distais."
  },
  {
    title: "Caso 6",
    text: "A pessoa ajusta o tronco automaticamente antes de empurrar uma porta pesada.",
    answer: "Postura",
    why: "Esse ajuste antes do movimento é antecipatório e faz parte do controle postural."
  }
];

const checklistItems = [
  "Explico a diferença entre córtex, tronco, medula e músculo.",
  "Diferencio córtex motor primário, pré-motor e suplementar.",
  "Consigo desenhar o caminho do trato corticoespinal.",
  "Sei por que a decussação das pirâmides importa.",
  "Comparo vias corticoespinais e extrapiramidais.",
  "Relaciono propriocepção, vestibular e visão ao equilíbrio.",
  "Reconheço NMS, NMI e cerebelar em casos clínicos."
];

const storage = {
  get(key, fallback) {
    try {
      const value = window.localStorage.getItem(key);
      return value ? JSON.parse(value) : fallback;
    } catch {
      return fallback;
    }
  },
  set(key, value) {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch {
      // Navegadores podem bloquear localStorage em paginas blob/data.
      // O app continua funcionando; apenas nao persiste progresso.
    }
  }
};

const state = {
  activeModule: 0,
  activeSlide: 0,
  cardIndex: 0,
  cardFlipped: false,
  quizIndex: 0,
  quizScore: 0,
  quizSelected: null,
  completed: new Set(storage.get("pl.completed", [])),
  mastered: new Set(storage.get("pl.mastered", []))
};

const scene02Topics = {
  sulcus:
    "Sulco Central: não é uma área cortical; é um sulco anatômico, uma linha de fronteira que separa o giro pré-central do giro pós-central. É a referência essencial para localizar áreas motoras e sensitivas.",
  motor:
    "Área Motora Primária: localizada no giro pré-central. Participa da execução dos movimentos voluntários. Lesões podem causar fraqueza ou paralisia contralateral.",
  sensory:
    "Área Somatossensorial Primária: localizada no giro pós-central. Recebe informações de tato, dor, temperatura, pressão e propriocepção. Lesões podem causar perda sensitiva contralateral."
};

const scene02Discoveries = {
  sulcus: {
    mode: "sulcus",
    title: "Linha revelada: fronteira anatômica",
    text:
      "O sulco central aparece como linha, não como área. Antes dele está o giro pré-central, ligado ao movimento; depois dele está o giro pós-central, ligado à sensibilidade.",
    chips: ["Sulco = linha", "Antes = motor", "Depois = sensibilidade", "Fronteira cortical"]
  },
  motor: {
    mode: "motor",
    title: "Função revelada: movimento voluntário",
    text:
      "Ao selecionar o giro pré-central, associe a área vermelha à execução de movimentos voluntários e ao comando motor contralateral.",
    chips: ["Movimento voluntário", "Execução motora", "Força contralateral"]
  },
  sensory: {
    mode: "sensory",
    title: "Função revelada: tato, dor e temperatura",
    text:
      "Ao selecionar o giro pós-central, associe a área azul à chegada das informações sensitivas que ajudam o corpo a perceber o ambiente e a posição.",
    chips: ["Tato", "Dor", "Temperatura", "Pressão", "Propriocepção"]
  }
};

const scene03Topics = {
  hand: {
    label: "Mão",
    image: "../Imagens/Cena 03/Cena03_mão.png",
    imageAlt: "Representação anatômica da mão",
    title: "Representação Cortical da Mão",
    description:
      "A mão ocupa uma das maiores áreas do córtex somatossensorial devido à enorme densidade de receptores táteis e à necessidade de movimentos extremamente precisos.",
    clinical: "Alterações nessa região podem comprometer destreza fina e percepção tátil.",
    curiosity: "A área cortical destinada à mão é muito maior do que seu tamanho físico sugeriria."
  },
  face: {
    label: "Face",
    image: "../Imagens/Cena 03/Cena03_face.png",
    imageAlt: "Representação anatômica da face",
    title: "Representação Cortical da Face",
    description:
      "A face possui elevada sensibilidade tátil e desempenha papel essencial na comunicação, expressão emocional e proteção.",
    clinical: "Lesões podem alterar percepção sensorial facial.",
    curiosity: "Pequenas regiões da face possuem enorme representação cortical."
  },
  tongue: {
    label: "Língua",
    image: "../Imagens/Cena 03/Cena03_lingua.png",
    imageAlt: "Representação anatômica da língua",
    title: "Representação Cortical da Língua",
    description:
      "A língua apresenta grande representação cortical devido à sua importância para fala, deglutição e percepção gustativa.",
    clinical: "Comprometimentos podem afetar articulação da fala.",
    curiosity: "A precisão motora da língua exige controle neural extremamente refinado."
  },
  foot: {
    label: "Pé",
    image: "../Imagens/Cena 03/Cena03_Pés.png",
    imageAlt: "Representação anatômica do pé",
    title: "Representação Cortical do Pé",
    description:
      "Os pés fornecem informações constantes sobre equilíbrio, pressão e posicionamento corporal.",
    clinical: "Alterações sensoriais podem impactar postura e marcha.",
    curiosity: "Mesmo distante da face e mãos, o pé possui representação cortical claramente definida."
  }
};

let scene03TransitionTimer = null;

const els = {
  progressText: document.getElementById("progressText"),
  progressBar: document.getElementById("progressBar"),
  moduleList: document.getElementById("moduleList"),
  moduleContent: document.getElementById("moduleContent"),
  slideThumbs: document.getElementById("slideThumbs"),
  slideStage: document.getElementById("slideStage"),
  slideNotes: document.getElementById("slideNotes"),
  flashcard: document.getElementById("flashcard"),
  cardCounter: document.getElementById("cardCounter"),
  quizPanel: document.getElementById("quizPanel"),
  caseGrid: document.getElementById("caseGrid"),
  reviewChecklist: document.getElementById("reviewChecklist"),
  sensorResult: document.getElementById("sensorResult"),
  anatomyFrame: document.getElementById("anatomyFrame"),
  slides3dFrame: document.getElementById("slides3dFrame")
};

function persist() {
  storage.set("pl.completed", [...state.completed]);
  storage.set("pl.mastered", [...state.mastered]);
}

function renderProgress() {
  const total = modules.length + flashcards.length;
  const done = state.completed.size + state.mastered.size;
  const percent = Math.round((done / total) * 100);
  els.progressText.textContent = `${percent}%`;
  els.progressBar.style.width = `${percent}%`;
}

function setView(viewName) {
  document.querySelectorAll(".view").forEach((view) => view.classList.remove("is-active"));
  document.getElementById(`${viewName}View`).classList.add("is-active");
  document.querySelectorAll(".nav-button").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.view === viewName);
  });
  if (viewName === "anatomy") initAnatomy3D();
  if (viewName === "slides3d") initSlides3D();
}

function hideScene03() {
  const scene03 = document.getElementById("scene03");
  if (scene03) scene03.setAttribute("hidden", "");
}

function showScene02() {
  hideScene03();
  document.body.classList.add("has-started", "is-scene-02");
  document.body.classList.remove("is-scene-03");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showScene01() {
  hideScene03();
  document.body.classList.remove("has-started", "is-scene-02", "is-scene-03");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showLearningApp() {
  hideScene03();
  document.body.classList.add("has-started");
  document.body.classList.remove("is-scene-02", "is-scene-03");
  setView("modules");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showScene03() {
  const scene03 = document.getElementById("scene03");
  if (!scene03) {
    showLearningApp();
    return;
  }

  document.body.classList.add("has-started");
  document.body.classList.add("is-scene-03");
  document.body.classList.remove("is-scene-02");
  scene03.removeAttribute("hidden");
  setScene03Topic(scene03.dataset.active || "hand", true);
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function openSceneFile(fileName) {
  window.location.href = fileName;
}

function setScene02Topic(topic) {
  const scene = document.getElementById("scene02");
  const panelText = document.getElementById("scene02PanelText");
  if (!scene || !panelText || !scene02Topics[topic]) return;

  scene.dataset.active = topic;
  panelText.textContent = scene02Topics[topic];
  renderScene02Discovery(topic);
  document.querySelectorAll("[data-scene02-topic]").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.scene02Topic === topic);
  });
}

function renderScene02Discovery(topic) {
  const discovery = scene02Discoveries[topic];
  const box = document.getElementById("scene02Discovery");
  const title = document.getElementById("scene02DiscoveryTitle");
  const text = document.getElementById("scene02DiscoveryText");
  const chips = document.getElementById("scene02DiscoveryChips");
  if (!discovery || !box || !title || !text || !chips) return;

  box.dataset.mode = discovery.mode;
  title.textContent = discovery.title;
  text.textContent = discovery.text;
  chips.replaceChildren(
    ...discovery.chips.map((chip) => {
      const item = document.createElement("span");
      item.textContent = chip;
      return item;
    })
  );
}

function setScene03Topic(topic, instant = false) {
  const data = scene03Topics[topic];
  const scene = document.getElementById("scene03");
  const card = document.getElementById("scene03Card");
  const image = document.getElementById("scene03CardImage");
  const kicker = document.getElementById("scene03CardKicker");
  const title = document.getElementById("scene03CardTitle");
  const description = document.getElementById("scene03CardDescription");
  const clinical = document.getElementById("scene03CardClinical");
  const curiosity = document.getElementById("scene03CardCuriosity");
  if (!data || !scene || !card || !image || !kicker || !title || !description || !clinical || !curiosity) return;

  clearTimeout(scene03TransitionTimer);
  scene.dataset.active = topic;
  document.querySelectorAll("[data-scene03-topic]").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.scene03Topic === topic);
  });

  const updateCard = () => {
    image.src = data.image;
    image.alt = data.imageAlt;
    kicker.textContent = `Região selecionada · ${data.label}`;
    title.textContent = data.title;
    description.textContent = data.description;
    clinical.textContent = data.clinical;
    curiosity.textContent = data.curiosity;
  };

  if (instant) {
    card.classList.remove("is-fading");
    updateCard();
    return;
  }

  card.classList.add("is-fading");
  scene03TransitionTimer = setTimeout(() => {
    updateCard();
    card.classList.remove("is-fading");
  }, 170);
}

function answerScene02Quiz(button) {
  const feedback = document.getElementById("scene02QuizFeedback");
  if (!feedback) return;

  const isCorrect = button.dataset.scene02Answer === "correct";
  document.querySelectorAll("[data-scene02-answer]").forEach((item) => {
    item.classList.remove("is-correct", "is-incorrect");
  });
  button.classList.add(isCorrect ? "is-correct" : "is-incorrect");
  feedback.className = `scene-02__feedback ${isCorrect ? "is-good" : "is-bad"}`;
  feedback.textContent = isCorrect
    ? "Correto. O sulco central é a principal referência anatômica entre o córtex motor e o córtex somatossensorial."
    : "Revise a regra: antes do sulco central é motor; depois do sulco central é sensitivo.";
}

function decodePortableHtml(payload) {
  const binary = atob(payload);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i += 1) bytes[i] = binary.charCodeAt(i);
  return new TextDecoder("utf-8").decode(bytes);
}

function initAnatomy3D() {
  if (!els.anatomyFrame || els.anatomyFrame.dataset.loaded === "true") return;
  if (window.embeddedAnatomyHtml) {
    els.anatomyFrame.srcdoc = decodePortableHtml(window.embeddedAnatomyHtml);
  } else {
    els.anatomyFrame.src = "ANATOMIA_3D.html";
  }
  els.anatomyFrame.dataset.loaded = "true";
}

function initSlides3D() {
  if (!els.slides3dFrame || els.slides3dFrame.dataset.loaded === "true") return;
  if (window.embeddedSlides3dHtml) {
    els.slides3dFrame.srcdoc = decodePortableHtml(window.embeddedSlides3dHtml);
  } else {
    els.slides3dFrame.src = "LAMINAS_3D.html";
  }
  els.slides3dFrame.dataset.loaded = "true";
}

function renderModules() {
  els.moduleList.innerHTML = modules
    .map((module, index) => {
      const done = state.completed.has(module.id) ? "Dominado" : module.time;
      return `<button class="module-button ${index === state.activeModule ? "is-active" : ""}" data-module="${index}" type="button">
        <strong>${module.title}</strong>
        <span>${done}</span>
      </button>`;
    })
    .join("");

  document.querySelectorAll("[data-module]").forEach((button) => {
    button.addEventListener("click", () => {
      state.activeModule = Number(button.dataset.module);
      renderModules();
    });
  });

  renderModuleContent();
}

function renderModuleContent() {
  const module = modules[state.activeModule];
  const isDone = state.completed.has(module.id);
  const sourceButtons = module.slides
    .map((number) => `<button class="source-link" data-slide-jump="${number}" type="button">Lâmina ${number}</button>`)
    .join("");
  const anatomyButton = `<button class="source-link" data-open-anatomy="${module.slides[0] - 1}" type="button">Anatomia 3D</button>`;
  const sceneButtons = (module.sceneLinks || [])
    .map((scene) => `<a class="source-link" href="${scene.href}">${scene.label}</a>`)
    .join("");

  els.moduleContent.innerHTML = `
    <h3>${module.title}</h3>
    <div class="module-meta">
      <span class="pill">${module.time}</span>
      <span class="pill wine">${isDone ? "Concluído" : "Em estudo"}</span>
      <span class="pill amber">Lâminas ${module.slides.join(", ")}</span>
    </div>
    <p class="lead">${module.summary}</p>
    <div class="concept-grid">
      ${module.concepts.map(([title, text]) => `<div class="concept-card"><h4>${title}</h4><p>${text}</p></div>`).join("")}
    </div>
    <div class="callout"><strong>Como cai em prova:</strong> ${module.exam}</div>
    <p><strong>Objetivo:</strong> ${module.goal}</p>
    <div class="source-strip">${sourceButtons}${anatomyButton}${sceneButtons}</div>
    <div class="module-actions">
      <button id="completeModule" class="primary-button" type="button">${isDone ? "Marcar como não concluído" : "Marcar módulo como concluído"}</button>
      <button id="openModuleQuiz" class="ghost-button" type="button">Treinar no quiz</button>
    </div>
  `;

  document.getElementById("completeModule").addEventListener("click", () => {
    if (state.completed.has(module.id)) {
      state.completed.delete(module.id);
    } else {
      state.completed.add(module.id);
    }
    persist();
    renderProgress();
    renderModules();
  });

  document.getElementById("openModuleQuiz").addEventListener("click", () => setView("quiz"));

  document.querySelectorAll("[data-slide-jump]").forEach((button) => {
    button.addEventListener("click", () => {
      state.activeSlide = Number(button.dataset.slideJump) - 1;
      renderAtlas();
      setView("atlas");
    });
  });

  document.querySelectorAll("[data-open-anatomy]").forEach((button) => {
    button.addEventListener("click", () => {
      const index = Number(button.dataset.openAnatomy);
      setView("anatomy");
      setTimeout(() => {
        if (els.anatomyFrame && els.anatomyFrame.contentWindow) {
          els.anatomyFrame.contentWindow.postMessage({ type: "setScene", index }, "*");
        }
      }, 120);
    });
  });
}

function renderAtlas() {
  els.slideThumbs.innerHTML = slides
    .map((slide, index) => `<button class="thumb-button ${index === state.activeSlide ? "is-active" : ""}" data-slide="${index}" type="button">
      <img src="${slide.src}" alt="">
      <span>${slide.number}. ${slide.title}</span>
    </button>`)
    .join("");

  document.querySelectorAll("[data-slide]").forEach((button) => {
    button.addEventListener("click", () => {
      state.activeSlide = Number(button.dataset.slide);
      renderAtlas();
    });
  });

  const slide = slides[state.activeSlide];
  els.slideStage.innerHTML = `<img class="${slide.rotate ? "rotate90" : ""}" src="${slide.src}" alt="Lâmina ${slide.number}: ${slide.title}">`;
  
  const anatomyBtn = `<button class="source-link" data-open-anatomy="${slide.number - 1}" type="button">Explorar Anatomia 3D</button>`;
  const slides3dBtn = `<button class="source-link" data-open-slides3d="${slide.number - 1}" type="button">Explorar em Lâminas 3D</button>`;

  els.slideNotes.innerHTML = `<h3>Lâmina ${slide.number}: ${slide.title}</h3><p>${slide.note}</p><div class="source-strip">${anatomyBtn}${slides3dBtn}</div>`;

  document.querySelectorAll("[data-open-anatomy]").forEach((button) => {
    button.addEventListener("click", () => {
      const index = Number(button.dataset.openAnatomy);
      setView("anatomy");
      setTimeout(() => {
        if (els.anatomyFrame && els.anatomyFrame.contentWindow) {
          els.anatomyFrame.contentWindow.postMessage({ type: "setScene", index }, "*");
        }
      }, 120);
    });
  });

  document.querySelectorAll("[data-open-slides3d]").forEach((button) => {
    button.addEventListener("click", () => {
      const slideIndex = Number(button.dataset.openSlides3d);
      setView("slides3d");
      setTimeout(() => {
        if (els.slides3dFrame && els.slides3dFrame.contentWindow) {
          els.slides3dFrame.contentWindow.postMessage({ type: "setSlide", index: slideIndex }, "*");
        }
      }, 120);
    });
  });
}

function moveSlide(offset) {
  state.activeSlide = (state.activeSlide + offset + slides.length) % slides.length;
  renderAtlas();
}

function renderFlashcard() {
  const card = flashcards[state.cardIndex];
  const mastered = state.mastered.has(card.id);
  els.flashcard.innerHTML = `<div>
    <strong>${state.cardFlipped ? "Resposta" : "Pergunta"}</strong>
    <span>${state.cardFlipped ? card.a : card.q}</span>
  </div>`;
  els.cardCounter.textContent = `Cartão ${state.cardIndex + 1} de ${flashcards.length}${mastered ? " | dominado" : ""}`;
  document.getElementById("markCard").textContent = mastered ? "Remover domínio" : "Marcar como dominado";
}

function moveCard(offset) {
  state.cardIndex = (state.cardIndex + offset + flashcards.length) % flashcards.length;
  state.cardFlipped = false;
  renderFlashcard();
}

function renderQuiz() {
  if (state.quizIndex >= quiz.length) {
    const percent = Math.round((state.quizScore / quiz.length) * 100);
    els.quizPanel.innerHTML = `
      <div class="quiz-question">
        <h3>Resultado: ${state.quizScore}/${quiz.length}</h3>
        <p class="lead">${percent >= 80 ? "Excelente. Você já está raciocinando pela lógica da aula." : "Bom treino. Revise os módulos com menor segurança e refaça o quiz."}</p>
        <div class="callout"><strong>Meta:</strong> mire 80% ou mais sem consultar as lâminas.</div>
        <button id="finishRestart" class="primary-button" type="button">Refazer quiz</button>
      </div>`;
    document.getElementById("finishRestart").addEventListener("click", restartQuiz);
    return;
  }

  const item = quiz[state.quizIndex];
  els.quizPanel.innerHTML = `
    <div class="quiz-question">
      <p class="muted">Questão ${state.quizIndex + 1} de ${quiz.length}</p>
      <h3>${item.q}</h3>
      <div class="answers">
        ${item.options
          .map((option, index) => {
            let cls = "";
            if (state.quizSelected !== null) {
              if (index === item.answer) cls = "correct";
              if (index === state.quizSelected && index !== item.answer) cls = "incorrect";
            }
            return `<button class="answer-button ${cls}" data-answer="${index}" type="button" ${state.quizSelected !== null ? "disabled" : ""}>${option}</button>`;
          })
          .join("")}
      </div>
      ${state.quizSelected !== null ? `<div class="feedback"><strong>${state.quizSelected === item.answer ? "Correto." : "Revise isso."}</strong> ${item.why}</div>` : ""}
      <div class="quiz-footer">
        <span class="muted">Pontuação: ${state.quizScore}</span>
        <button id="nextQuiz" class="${state.quizSelected === null ? "ghost-button" : "primary-button"}" type="button">${state.quizSelected === null ? "Responder para avançar" : "Próxima"}</button>
      </div>
    </div>`;

  document.querySelectorAll("[data-answer]").forEach((button) => {
    button.addEventListener("click", () => {
      const selected = Number(button.dataset.answer);
      state.quizSelected = selected;
      if (selected === item.answer) state.quizScore += 1;
      renderQuiz();
    });
  });

  document.getElementById("nextQuiz").addEventListener("click", () => {
    if (state.quizSelected === null) return;
    state.quizIndex += 1;
    state.quizSelected = null;
    renderQuiz();
  });
}

function restartQuiz() {
  state.quizIndex = 0;
  state.quizScore = 0;
  state.quizSelected = null;
  renderQuiz();
}

function renderCases() {
  els.caseGrid.innerHTML = cases
    .map((item, index) => `<article class="case-card">
      <h3>${item.title}</h3>
      <p>${item.text}</p>
      <div class="case-options">
        ${["NMS", "NMI", "Cerebelar", "Sensorial", "Corticoespinal", "Postura"]
          .map((option) => `<button class="case-option" data-case="${index}" data-case-answer="${option}" type="button">${option}</button>`)
          .join("")}
      </div>
      <div id="case-feedback-${index}" class="case-feedback">Escolha a melhor classificação.</div>
    </article>`)
    .join("");

  document.querySelectorAll("[data-case]").forEach((button) => {
    button.addEventListener("click", () => {
      const item = cases[Number(button.dataset.case)];
      const answer = button.dataset.caseAnswer;
      const box = document.getElementById(`case-feedback-${button.dataset.case}`);
      const good = answer === item.answer;
      box.className = `case-feedback ${good ? "good" : "bad"}`;
      box.innerHTML = `<strong>${good ? "Acertou." : `Melhor resposta: ${item.answer}.`}</strong> ${item.why}`;
    });
  });
}

function renderChecklist() {
  const saved = storage.get("pl.checklist", []);
  els.reviewChecklist.innerHTML = checklistItems
    .map((item, index) => `<label><input type="checkbox" data-check="${index}" ${saved.includes(index) ? "checked" : ""}> ${item}</label>`)
    .join("");

  document.querySelectorAll("[data-check]").forEach((input) => {
    input.addEventListener("change", () => {
      const checked = [...document.querySelectorAll("[data-check]:checked")].map((el) => Number(el.dataset.check));
      storage.set("pl.checklist", checked);
    });
  });
}

function updateSensorLab() {
  const proprio = document.getElementById("senseProprio").checked;
  const vestibular = document.getElementById("senseVestibular").checked;
  const vision = document.getElementById("senseVision").checked;
  const active = [proprio, vestibular, vision].filter(Boolean).length;
  let message = "";

  if (active === 3) {
    message = "Integração forte: o corpo tem posição articular, aceleração da cabeça e referência visual para ajustar postura e movimento.";
  } else if (active === 2) {
    message = "Controle possível, mas mais vulnerável. O sistema restante precisa compensar a fonte ausente.";
  } else if (active === 1) {
    message = "Controle instável. Com apenas uma fonte sensorial, aumentam erros de orientação, equilíbrio e correção.";
  } else {
    message = "Sem feedback sensorial, o comando motor perde referência para ajustar postura e movimento.";
  }

  els.sensorResult.textContent = message;
}

document.querySelectorAll(".nav-button").forEach((button) => {
  button.addEventListener("click", () => setView(button.dataset.view));
});

const startSceneButton = document.getElementById("startScene");
if (startSceneButton) {
  startSceneButton.addEventListener("click", () => {
    showScene02();
  });
}

document.querySelectorAll("[data-scene02-topic]").forEach((button) => {
  button.addEventListener("click", () => setScene02Topic(button.dataset.scene02Topic));
});

document.querySelectorAll("[data-scene02-answer]").forEach((button) => {
  button.addEventListener("click", () => answerScene02Quiz(button));
});

document.querySelectorAll("[data-scene03-topic]").forEach((button) => {
  button.addEventListener("click", () => setScene03Topic(button.dataset.scene03Topic));
});

const backToScene01Button = document.getElementById("backToScene01");
if (backToScene01Button) {
  backToScene01Button.addEventListener("click", showScene01);
}

const nextSceneButton = document.getElementById("nextSceneButton");
if (nextSceneButton) {
  nextSceneButton.addEventListener("click", () => openSceneFile("cena03_homunculo_sensorial_1.html"));
}

const backToScene02Button = document.getElementById("backToScene02");
if (backToScene02Button) {
  backToScene02Button.addEventListener("click", showScene02);
}

const nextFromScene03Button = document.getElementById("nextFromScene03");
if (nextFromScene03Button) {
  nextFromScene03Button.addEventListener("click", () => openSceneFile("cena04_trato_corticoespinhal.html"));
}

setScene03Topic("hand", true);

document.getElementById("resetProgress").addEventListener("click", () => {
  state.completed.clear();
  state.mastered.clear();
  persist();
  renderProgress();
  renderModules();
  renderFlashcard();
});

document.getElementById("prevSlide").addEventListener("click", () => moveSlide(-1));
document.getElementById("nextSlide").addEventListener("click", () => moveSlide(1));
document.getElementById("prevCard").addEventListener("click", () => moveCard(-1));
document.getElementById("nextCard").addEventListener("click", () => moveCard(1));
document.getElementById("flipCard").addEventListener("click", () => {
  state.cardFlipped = !state.cardFlipped;
  renderFlashcard();
});
document.getElementById("flashcard").addEventListener("click", () => {
  state.cardFlipped = !state.cardFlipped;
  renderFlashcard();
});
document.getElementById("markCard").addEventListener("click", () => {
  const id = flashcards[state.cardIndex].id;
  if (state.mastered.has(id)) {
    state.mastered.delete(id);
  } else {
    state.mastered.add(id);
  }
  persist();
  renderProgress();
  renderFlashcard();
});
document.getElementById("restartQuiz").addEventListener("click", restartQuiz);
["senseProprio", "senseVestibular", "senseVision"].forEach((id) => {
  document.getElementById(id).addEventListener("change", updateSensorLab);
});

renderProgress();
renderModules();
renderAtlas();
renderFlashcard();
renderQuiz();
renderCases();
renderChecklist();
updateSensorLab();

if (window.location.hash === "#scene02") {
  showScene02();
}
