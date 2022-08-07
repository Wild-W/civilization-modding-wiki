---
tags:
- EffectType
title: EFFECT_GRANT_YIELD_PER_EXCESS_LUXURIES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_YIELD_PER_EXCESS_LUXURIES
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* YieldType `Unknown`

## Samples
```SQL {title="PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_EXCESS_LUXURIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_EXCESS_LUXURIES",
		"MODIFIER_PLAYER_GRANT_YIELD_PER_EXCESS_LUXURIES",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_EXCESS_LUXURIES",
		"Amount",
		50
	),
	(
		"PROJECT_COMPLETION_GRANT_CULTURE_BASED_ON_EXCESS_LUXURIES",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

