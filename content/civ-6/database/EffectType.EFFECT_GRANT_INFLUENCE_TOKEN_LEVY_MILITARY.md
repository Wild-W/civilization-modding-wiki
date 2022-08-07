---
tags:
- EffectType
title: EFFECT_GRANT_INFLUENCE_TOKEN_LEVY_MILITARY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_INFLUENCE_TOKEN_LEVY_MILITARY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="LEVY_MILITARY_TWO_FREE_ENVOYS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"LEVY_MILITARY_TWO_FREE_ENVOYS",
		"MODIFIER_PLAYER_ADJUST_ENVOYS_FROM_LEVIED_CITY_STATES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LEVY_MILITARY_TWO_FREE_ENVOYS",
		"Amount",
		2
	);
	
```

