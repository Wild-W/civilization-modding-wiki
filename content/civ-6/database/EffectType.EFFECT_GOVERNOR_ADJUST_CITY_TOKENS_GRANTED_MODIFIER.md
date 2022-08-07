---
tags:
- EffectType
title: EFFECT_GOVERNOR_ADJUST_CITY_TOKENS_GRANTED_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GOVERNOR_ADJUST_CITY_TOKENS_GRANTED_MODIFIER
>
> * Class: `GOVERNORS`
> * Parameters:
>	* Percent `Integer`

## Samples
```SQL {title="AMBASSADOR_ADJUST_CITY_ENVOY_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"AMBASSADOR_ADJUST_CITY_ENVOY_MODIFIER",
		"MODIFIER_GOVERNOR_ADJUST_CITY_ENVOYS_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AMBASSADOR_ADJUST_CITY_ENVOY_MODIFIER",
		"Percent",
		100
	);
	
```

