---
tags:
- EffectType
title: EFFECT_ALLIANCE_RESEARCH_AGREEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ALLIANCE_RESEARCH_AGREEMENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ALLIANCE_RESEARCH_AGREEMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ALLIANCE_RESEARCH_AGREEMENT",
		"MODIFIER_ALLIANCE_RESEARCH_AGREEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLIANCE_RESEARCH_AGREEMENT",
		"Amount",
		30
	);
	
```

