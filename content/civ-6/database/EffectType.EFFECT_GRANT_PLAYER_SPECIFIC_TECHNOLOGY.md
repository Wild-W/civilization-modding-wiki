---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_SPECIFIC_TECHNOLOGY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_SPECIFIC_TECHNOLOGY
>
> * Class: `PLAYERS`
> * Parameters:
>	* TechType `String`
>		* [Technologies.TechnologyType]

## Samples

```SQL {title="TRAIT_MAORI_MANA_SAILING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_MAORI_MANA_SAILING",
		"MODIFIER_PLAYER_GRANT_SPECIFIC_TECHNOLOGY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_MAORI_MANA_SAILING",
		"TechType",
		"TECH_SAILING"
	);
	
```

