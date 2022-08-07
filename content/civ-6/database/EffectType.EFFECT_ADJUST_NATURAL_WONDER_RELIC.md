---
tags:
- EffectType
title: EFFECT_ADJUST_NATURAL_WONDER_RELIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_NATURAL_WONDER_RELIC
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="MINOR_CIV_KANDY_GRANT_RELIC_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_KANDY_GRANT_RELIC_BONUS",
		"MODIFIER_PLAYER_ADJUST_NATURAL_WONDER_RELIC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_KANDY_GRANT_RELIC_BONUS",
		"Amount",
		1
	);
	
```

