---
tags:
- EffectType
title: EFFECT_GOVERNOR_ADJUST_CITY_TOKENS_GRANTED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GOVERNOR_ADJUST_CITY_TOKENS_GRANTED
>
> * Class: `GOVERNORS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MESSENGER_GRANT_FREE_ENVOYS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MESSENGER_GRANT_FREE_ENVOYS",
		"MODIFIER_GOVERNOR_ADJUST_CITY_ENVOYS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MESSENGER_GRANT_FREE_ENVOYS",
		"Amount",
		2
	);
	
```

