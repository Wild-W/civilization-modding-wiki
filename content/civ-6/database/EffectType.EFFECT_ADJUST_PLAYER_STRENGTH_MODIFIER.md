---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_STRENGTH_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_STRENGTH_MODIFIER
>
> * Class: `COMBATS`
> * Parameters:
>	* AdvancedStartMultiplier `Unknown`
>	* Amount `Integer`
>	* InversePlayerScaling `Unknown`
>	* Key `Unknown`
>	* Max `Unknown`
>	* Scalar `Unknown`

## Samples
```SQL {title="TOWERDEFENSE_ZOMBIE_COMBAT_STRENGTH_FROM_PROPERTY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TOWERDEFENSE_ZOMBIE_COMBAT_STRENGTH_FROM_PROPERTY",
		"MODIFIER_UNIT_ADJUST_COMBAT_STRENGTH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TOWERDEFENSE_ZOMBIE_COMBAT_STRENGTH_FROM_PROPERTY",
		"AdvancedStartMultiplier",
		50
	),
	(
		"TOWERDEFENSE_ZOMBIE_COMBAT_STRENGTH_FROM_PROPERTY",
		"InversePlayerScaling",
		1
	),
	(
		"TOWERDEFENSE_ZOMBIE_COMBAT_STRENGTH_FROM_PROPERTY",
		"Key",
		"GAME_NUMBER_OF_ZOMBIE_DEATHS"
	),
	(
		"TOWERDEFENSE_ZOMBIE_COMBAT_STRENGTH_FROM_PROPERTY",
		"Scalar",
		"0.5"
	);
	
```

```SQL {title="DEFENDER_OF_FAITH_COMBAT_BONUS_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DEFENDER_OF_FAITH_COMBAT_BONUS_MODIFIER",
		"MODIFIER_UNIT_ADJUST_COMBAT_STRENGTH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DEFENDER_OF_FAITH_COMBAT_BONUS_MODIFIER",
		"Amount",
		5
	);
	
```

```SQL {title="SANGUINE_PACT_VAMPIRE_COMBAT_STRENGTH_FROM_PROPERTY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SANGUINE_PACT_VAMPIRE_COMBAT_STRENGTH_FROM_PROPERTY",
		"MODIFIER_UNIT_ADJUST_COMBAT_STRENGTH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SANGUINE_PACT_VAMPIRE_COMBAT_STRENGTH_FROM_PROPERTY",
		"Key",
		"COMBAT_STRENGTH_FOR_VAMPIRISM"
	);
	
```

```SQL {title="SANGUINE_PACT_VAMPIRE_BARB_COMBAT_STRENGTH_FROM_PROPERTY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SANGUINE_PACT_VAMPIRE_BARB_COMBAT_STRENGTH_FROM_PROPERTY",
		"MODIFIER_UNIT_ADJUST_COMBAT_STRENGTH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SANGUINE_PACT_VAMPIRE_BARB_COMBAT_STRENGTH_FROM_PROPERTY",
		"Key",
		"COMBAT_STRENGTH_FOR_VAMPIRISM_BARB"
	),
	(
		"SANGUINE_PACT_VAMPIRE_BARB_COMBAT_STRENGTH_FROM_PROPERTY",
		"Max",
		10
	);
	
```

