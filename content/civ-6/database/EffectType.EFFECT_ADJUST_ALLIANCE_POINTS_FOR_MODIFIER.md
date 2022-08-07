---
tags:
- EffectType
title: EFFECT_ADJUST_ALLIANCE_POINTS_FOR_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALLIANCE_POINTS_FOR_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="ARSENALOFDEMOCRACY_ALLIANCEPOINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ARSENALOFDEMOCRACY_ALLIANCEPOINTS",
		"MODIFIER_PLAYER_ADJUST_ALLIANCE_POINTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ARSENALOFDEMOCRACY_ALLIANCEPOINTS",
		"Amount",
		1
	);
	
```

