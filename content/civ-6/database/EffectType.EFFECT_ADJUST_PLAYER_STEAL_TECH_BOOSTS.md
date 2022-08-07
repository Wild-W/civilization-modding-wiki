---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_STEAL_TECH_BOOSTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_STEAL_TECH_BOOSTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="NUCLEARESPIONAGE_EXTRABOOSTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NUCLEARESPIONAGE_EXTRABOOSTS",
		"MODIFIER_PLAYER_ADJUST_STEAL_TECH_BOOSTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NUCLEARESPIONAGE_EXTRABOOSTS",
		"Amount",
		1
	);
	
```

